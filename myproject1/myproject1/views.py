from os import remove
import re
from ssl import Purpose
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')


def analyze(request):
    txt = request.POST.get('text', 'default')
    removpunc = request.POST.get('removpunc', 'off')
    caps = request.POST.get('caps','off')
    count = request.POST.get('count','off')
    if removpunc == "on":
        analyzed = ""
        punc = ''' !@#$%^&*()_+<>?:"{}[];'./ '''
        for i in txt:
         if i not in punc:
           analyzed = analyzed+i
        dict = { 'purpose' : "Removed Punctuations", 'analyzed_text': analyzed}
        return render(request,'analyze.html',dict)
    
    elif(caps == "on"):
        analyzed = ""
        for i in txt:
            analyzed = analyzed + i.upper()
        dict = { 'purpose' : "Capitalize text", 'analyzed_text': analyzed}
        return render(request,'analyze.html',dict)
    elif(count == "on"):
        analyzed = len(txt)
        
        dict = { 'purpose' : "Count text", 'analyzed_text': analyzed}
        return render(request,'analyze.html',dict)

#    elif(removpunc == "on") and caps == "on" and count == "on":



    else:
        return HttpResponse("Please tick the checkbutton then your text will be analyzed!!!!!!")
    
    