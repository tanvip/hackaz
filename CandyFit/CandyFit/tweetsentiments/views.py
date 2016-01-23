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
            print("anupam")
            Company_id = form.cleaned_data['Company_id']
            Job_Title = form.cleaned_data['Job_Title']
            print my_con.tweetsentiments_candidate.find({ Job_Title: form.cleaned_data['Job_Title'] });
    return render_to_response('index.html',{'form': form, 'results':response,},context_instance = RequestContext(request))

def home(request):
    response = ""
    calc = {
                "positive":0.0,
                "negative":0.0,
                "neutral":0.0
                }
    if request.method == 'GET':
        form = Candiate_Form()
    else:
        # A POST request: Handle Form Upload
        form = Candiate_Form(request.POST) # Bind data from request.POST into a PostForm
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
            item = companyinfo( Description = form1.cleaned_data['Description'], Job_Title = form1.cleaned_data['Job_Title'], Company_Name = form1.cleaned_data['Company_Name'], Perks = form1.cleaned_data['Perks'], Activities = form1.cleaned_data['Activities'] )
            item.save()
    return render_to_response('company.html',{'form': form1,},context_instance = RequestContext(request))