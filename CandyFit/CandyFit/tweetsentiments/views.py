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
import graphlab
import json
from pprint import pprint


# In[3]:
import string
import nltk
import csv
import codecs


my_con = connect('Info', alias='Default')

TFratio = 0.6
minTweets = 10

import math
def category_score(rootDict, userTFIDFDict):
    lst= []

    score = 0
    sqr = 0
    for word in rootDict:
        if word in userTFIDFDict:
            tfidf = userTFIDFDict[word]
            score = score + tfidf
            sqr = sqr + tfidf * tfidf
        if sqr==0:
            score=0
        else:
                score = score / (math.sqrt(sqr) * math.sqrt(len(rootDict)))
    lst.append(score * 100)
    #print score
    return lst



def analyser(request):
    response = ""
    results = {}
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
            stopWords = nltk.corpus.stopwords.words('english') + ['.',',']
            stopWords.append('tx')
            name_list = list()
            profile_list = list()
            for i in candidate.find({ 'Job_Title': form.cleaned_data['Job_Title']}):
                elem = list()
                name = i['Name']
                results[name]={}
                elem.append(i['Extra_Curricular'])
                elem.append(i['Cover_Title'])
                l = ' '.join(elem)
                l = l.encode("utf-8")

                name_list.append(name)
                profile_list.append(l)
                #import pdb; pdb.set_trace()

            Name_Sarray = graphlab.SArray(name_list)
            Profile_Sarray = graphlab.SArray(profile_list)
            sf = graphlab.SFrame({'name': Name_Sarray, 'profile' : Profile_Sarray})
            sf['word_count'] = graphlab.text_analytics.count_words(sf['profile'])
            tfidf = graphlab.text_analytics.tf_idf(sf['word_count'])
            sf['tfidf'] = tfidf
            rootFrame = graphlab.SArray([{'Communication' : 1},{ 'self-motivated' : 1},{ 'hard-working' : 1},{ 'adaptive team' : 1},{ 'player' : 1},{ 'honest' : 1},{ 'descipline' : 1},{ 'passionate' : 1},{ 'goal-oriented' : 1},{ 'creative' : 1},{ 'confidence' : 1},{ 'positive' : 1},{ 'inspiration' : 1},{ 'Commitment' : 1},{ 'innovation' : 1},{ 'decision' : 1},{ 'making' : 1},{ 'trust' : 1 },{ 'motivator' : 1}])
            rootDict= {'Communication' : 1, 'self-motivated' : 1, 'hard-working' : 1, 'adaptive team' : 1, 'player' : 1, 'honest' : 1, 'descipline' : 1, 'passionate' : 1, 'goal-oriented' : 1, 'creative' : 1, 'confidence' : 1, 'positive' : 1, 'inspiration' : 1, 'Commitment' : 1, 'innovation' : 1, 'decision' : 1, 'making' : 1, 'trust' : 1 , 'motivator' : 1}
            import math
            score_List= []
            communication={
            "honest":1,
            "communication":1,
            "positive":1,
            "advice":1,
            "commute":1,
            "speaking":1,
            "speak":1,
            "talkig":1,
            "intelligence":1,
            "intelligent":1,
            "confidence":1,
            "skill":1,
            "verbal":1,
            "listener":1,
            "listen":1,
            "behavior":1,
            "feedback":1,
            "effective":1,
            "interpersonal":1,
            "interperson":1,
            "workplace":1,
            "work":1,
            "good":1,
            "polite":1,
            "care":1,
            "people":1,
            "person":1,
            "personal":1

            }


            # In[3]:

            confidence={
            'bold': 1,
             'convinced': 1,
             'courageous': 1,
             'fearless': 1,
             'hopeful': 1,
             'positive': 1,
             'anguine': 1,
             'satisfied': 1,
             'self-assured': 1,
             'self-reliant': 1,
             'upbeat': 1,
             'brave': 1,
             'faith': 1,
             'dauntless': 1,
             'expectant': 1,
             'intrepid': 1,
             'presumptuous': 1,
             'puffed': 1,
             'valiant': 1,
              'puffed' : 1
            }


            # In[4]:

            goal_oriented={
              "determination": 1,
              "determined": 1,
              "ernest": 1,
              "ethusiastic": 1,
              "resource": 1,
              "eager": 1,
              "avid": 1,
              "result": 1,
              "goal-oriented":1,
              "goal":1,
              "aim":1,
              "target":1,
              "purpose":1,
              "high":1,
              "hopeful":1,
              "aspiraion":1,
              "driving":1,
              "belief":1,
              "believe":1,
              "plan":1,
              "planning":1,
              "strong":1,
              "dream":1,
              "dreams":1,
              "vision":1,
              "final":1


            }


            # In[5]:

            leadership={
             "admin":1,
             "administraion":1,
             "authority":1,
             "control":1,
             "manage":1,
             "skill":1,
             "capacity":1,
             "direction":1,
             "power":1,
             "initiative":1,
             "intitiate":1,
             "super":1,
             "superiority":1,
             "commit":1,
             "commitment":1,
             "delegation":1,
             "intutition":1,
             "inspire":1,
             "inspiration":1,
             "approach":1,
             "positive":1,
             "decision":1,
             "confidence":1

            }


            # In[6]:

            passionate={"affection": 1,
              "intensity": 1,
              "joy": 1,
              "happiness": 1,
              "happy": 1,
              "eager": 1,
              "eagerness": 1,
              "feeling": 1,
              "zeal": 1,
              "excitement": 1,
              "self": 1,
              "courage": 1,
              "courageous": 1,
              "focus": 1,
              "best": 1,
              "desire": 1,
              "trust": 1,
              "trustworthy": 1,
              "vision":1,
              "long-term":1,
              "longterm":1,
              "attitude":1,
              "actions":1,
              "action":1,
              "hard":1}


            # In[7]:

            recognition={
              "achievement": 1,
              "success": 1,
              "award": 1,
              "productive": 1,
              "acceptance": 1,
              "admission": 1,
              "undertanding": 1,
              "appreciation": 1,
              "perception": 1,
              "realization": 1,
              "respect": 1,
              "confession": 1,
              "memory": 1,
              "recollection": 1,
              "sensibility": 1,
              "decision": 1,
              "noticing": 1,
              "acknowledge": 1,
              "recall":1,
              "verifying":1,
              "detection":1,
              "salute":1,
              "identify:":1

            }


            # In[8]:

            team_player={
            "team":1,
            "player":1,
            "sports":1,
            "games":1,
            "help":1,
            "decision":1,
            "decision-making":1,
            "contribution":1,
            "adaptive":1,
            "flexible":1,
            "mixing":1,
            "friend":1,
            "friendly":1,
            "collabration":1,
            "collabrative":1,
            "group":1,
            "teamleader":1,
            "team-leader":1,
            "open":1,
            "talkative":1,
            "opinion":1,
            "helpful":1,
            "co-worker":1,
            "coworker":1
            }

            list_categories={}
            list_categories["communication"]=communication
            list_categories["confidence"]=confidence
            list_categories["goal_oriented"]=goal_oriented
            list_categories["leadership"]=leadership
            list_categories["passionate"]=passionate
            list_categories["recognition"]=recognition
            list_categories["team_player"]=team_player



            cat_score={}
            final_score = {}
            length = len(sf)
            #import pdb; pdb.set_trace()
            for j in range(0,length):
                for i in list_categories:
                    cat_score[i]=category_score(list_categories[i],sf['tfidf'][j])
                    cat_score['sentimental_score']=polarity_test(sf['profile'][j])
                final_score[sf['name'][j]]=cat_score
            print final_score

            for docDict in sf['tfidf']:
                score = 0
                sqr = 0
                for word in rootDict:
                    if word in docDict:
                        tfidf = docDict[word]
                        score = score + tfidf
                        sqr = sqr + tfidf * tfidf
                    if sqr==0:
                        score=0
                    else:
                        score = score / (math.sqrt(sqr) * math.sqrt(len(rootDict)))
                score_List.append(score * 100)
            #print score_List
            import json
            from json import load
            with open('data.txt', 'w') as outfile:
                json.dump(final_score, outfile)
            with open('data.txt', 'r') as file:
                 result = load(file)
            return render_to_response('dashboard.html',{'results':result,},context_instance = RequestContext(request))
    return render_to_response('analyser.html',{'form': form, 'results':results,},context_instance = RequestContext(request))

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