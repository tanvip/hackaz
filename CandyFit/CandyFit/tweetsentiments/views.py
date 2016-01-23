from django.shortcuts import render,RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import KeyForm
from pprint import pprint
from TwitterSentimentAnalysis.sentimentAnalyzer import *
	
# Create your views here.
#def home(request):
#    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

TFratio = 0.6
minTweets = 10

def home(request):
	response = ""
	calc = {
                "positive":0.0,
                "negative":0.0,
                "neutral":0.0
                }
	if request.method == 'GET':
		form = KeyForm()
	else:
		# A POST request: Handle Form Upload
		form = KeyForm(request.POST) # Bind data from request.POST into a PostForm
		# If data is valid, proceeds to create a new post and redirect the user
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
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
