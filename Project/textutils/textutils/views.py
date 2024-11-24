# I(Vivek) had created this file
from django.http import HttpResponse
from django.shortcuts import render  #for templates 

def index(request):
    return render(request,'index.html')

def analyze(request):
    dj_text =request.GET.get('text','default')
    print(dj_text)

    removepunc =request.GET.get('removepunc','off')
    print(removepunc)
   
    if removepunc == "on":
 
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        vivek = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',vivek)

    else:
        return HttpResponse("Eroor")

    

##################### This is the navigator code ##############################

# # I(Vivek) had created this file
# from django.http import HttpResponse
# from django.shortcuts import render  #for templates 

# def index(request):
#     return HttpResponse('<h1>Hello! This is the navigator bar</h1><p><ol>'
#                         '<li><a href="https://chatgpt.com/">Chatgpt</a></li> <br>'
#                         '<li><a href="https://gemini.google.com/app?hl=en-IN">Gemini</a></li> <br>'
#                         '<li><a href="https://claude.ai/login?returnTo=%2F%3F">Claude</a></li> <br></ol> </p>')

# def analyze(request):
#     dj_text =request.GET.get('text','default')
#     print(dj_text)

#     removepunc =request.GET.get('removepunc','off')
#     print(removepunc)
   
#     if removepunc == "on":
 
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed= ""
#         for char in dj_text:
#             if char not in punctuations:
#                 analyzed = analyzed + char
        
#         vivek = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
#         return render(request,'analyze.html',vivek)

#     else:
#         return HttpResponse("Eroor")






