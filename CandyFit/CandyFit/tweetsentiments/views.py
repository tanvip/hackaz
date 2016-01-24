from django.shortcuts import render,RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import *
from pprint import pprint
from TwitterSentimentAnalysis.sentimentAnalyzer import *
from models import *
# Create your views here.
#def home(request):
#    return render_to_response('index.html', locals(), context_instance = RequestContext(request))
from mongoengine import connect
import pymongo
from pymongo import MongoClient

my_con = connect('Info', alias='Default')

TFratio = 0.6
minTweets = 10

def analyser(request):
    response = ""
    calc = {
                "positive":0.0,
                "negative":0.0,
                "neutral":0.0
                }
    if request.method == 'GET':
        form = Analyse_Form()
    else:
        # A POST request: Handle Form Upload
        form = Analyse_Form(request.POST) # Bind data from request.POST into a PostForm
        if form.is_valid():
            #print("anupam")
            client = MongoClient()
            db = client.Info
            candidate = db.tweetsentiments_candidate
            Company_id = form.cleaned_data['Company_id']
            Job_Title = form.cleaned_data['Job_Title']
            results = {}
            for i in candidate.find({ 'Job_Title': form.cleaned_data['Job_Title']}):
                elem = list()
                name = i['Name']
                results[name]={}
                elem.append(i['Extra_Curricular'])
                elem.append(i['Cover_Title'])
                l = ' '.join(elem)
                l = l.encode("utf-8")
                #import pdb; pdb.set_trace()
                pol = polarity_test(l)
                results[name]['Sentimental_Analysis']=pol
                results[name]['Employee_Recognition']= 90.1
                results[name]['Passion']= 65.1
                results[name]['Goal_Oriented']= 85.1
                results[name]['Interest']= 90.1
                results[name]['Active']= 65.1

            print results
            import json
            with open('data.txt', 'w') as outfile:
                json.dump(results, outfile)
    return render_to_response('analyser.html',{'form': form, 'results':response,},context_instance = RequestContext(request))

def home(request):
    response = ""
    calc = {
                "positive":0.0,
                "negative":0.0,
                "neutral":0.0
                }
    if request.method == 'GET':
        form = Candidate_Form()
    else:
        # A POST request: Handle Form Upload
        form = Candidate_Form(request.POST) # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user

        if form.is_valid():
            print("anupam")
            keyword = form.cleaned_data['Name']
            item = candidate(Name=form.cleaned_data['Name'], Email = form.cleaned_data['Email'], Phone_Number = form.cleaned_data['Phone_Number'], Job_Title = form.cleaned_data['Job_Title'], Cover_Title = form.cleaned_data['Cover_Title'], Extra_Curricular = form.cleaned_data['Extra_Curricular'], Social_Profile = form.cleaned_data['Social_Profile']  )
            item.save()

            # newdoc = Document(docfile = request.FILES['docfile'])
            # newdoc.save()

            results = analyze(keyword)

            for i in results:
                    calc[i[3]]+=1
            ratio = (calc["positive"] if calc["positive"] > calc["negative"] else calc["negative"])/((calc["positive"]+calc["negative"]) or 1)
            pol = polarity_test(keyword).title()
            print "Ratio",ratio, calc, pol
            response = {
                    "polarity":pol,
                    "results":results,
                    "tf":"TRUTH" if (ratio > TFratio) and (len(results) >= minTweets) else "FALSE"
                        }
    return render_to_response('index.html',{'form': form, 'results':response,},context_instance = RequestContext(request))

def company(request):
    response = ""
    if request.method == 'GET':
        form1 = Company_Form()
    else:
        #import pdb; pdb.set_trace()
        # A POST request: Handle Form Upload
        form1 = Company_Form(request.POST) # Bind data from request.POST into a PostForm
        # If data is valid, proceeds to create a new post and redirect the user

        if form1.is_valid():
            pass
            item = companyinfo( Company_id = form1.cleaned_data['Company_id'],Description = form1.cleaned_data['Description'], Job_Title = form1.cleaned_data['Job_Title'], Company_Name = form1.cleaned_data['Company_Name'], Perks = form1.cleaned_data['Perks'], Activities = form1.cleaned_data['Activities'] )
            item.save()
    return render_to_response('company.html',{'form': form1,},context_instance = RequestContext(request))