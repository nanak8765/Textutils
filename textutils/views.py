#i have created this file.

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params  = {'name':'Biswajit', 'place':'Koraput'}
    return render(request, 'index.html')
    #return HttpResponse('''<h1>HOME</h1> <a href="https://biswajitportfolio.tech/">My Portfolio Website</a>''')

def about(request):
    return HttpResponse("About Me")

def ex1(request):
    return render(request,'ex1.html')
def analyze(request):
    djtext= request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
    #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
            djtext = analyzed
        #return render(request, 'analyze.html', params)

    if capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized ', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char != "\r"):
                analyzed = analyzed + char
            params = {'purpose': 'New Line Removed ', 'analyzed_text': analyzed}
            djtext = analyzed
        #return render(request, 'analyze.html', params)

    if extraspaceremove == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
            params = {'purpose': 'Extra Space Removed ', 'analyzed_text': analyzed}

    if (removepunc != "on" and capitalize != "on" and newlineremove != "on" and extraspaceremove != "on"):
        return HttpResponse("Please Select Any Operation and Try Again")

    return render(request, 'analyze.html', params)



'''def capitalizefirst(request):
    return HttpResponse("Capitalizefirst")
def newlineremove(request):
    return HttpResponse("New Line Remove")
def spaceremove(request):
    return HttpResponse("Space remove <a href='/'>Back</a>")
def charcount(request):
    return HttpResponse("Char Count")
'''