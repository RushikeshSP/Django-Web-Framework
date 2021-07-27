# I have created this file for views - Rushikesh.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text..
    djtext = request.POST.get('text', 'default')

    #Check checkbox values
    rempunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Analyse the text..
    punctuations = '''/[-[\]{}()*+?.;:>@%!_<,\^$|#\s]/g,'"\$&"'''

    if rempunc == 'on':
        analyzed = ""
        for char in djtext:
            if(char  not in punctuations):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Make It Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if (not ((djtext[index] == "  ") and (djtext[index+1] == " "))):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed


    if(rempunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on'):
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please Select a option and then analyse the text..")

