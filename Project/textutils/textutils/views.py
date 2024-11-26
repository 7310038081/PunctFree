# I(Vivek) had created this file
from django.http import HttpResponse
from django.shortcuts import render  #for templates 

def index(request):
    return render(request,'index.html')

def analyze(request):
    dj_text =request.GET.get('text','default') #Get the text 

    #check the checkbox values 
    removepunc =request.GET.get('removepunc','off')
    fullcaps =request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charcount = request.GET.get('charcount','off')

   #check which checkbox is on 
    if removepunc == "on":
 
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        vivek = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',vivek)
    
    elif(fullcaps=="on"):
        analyzed=""
        for char in dj_text:
            analyzed = analyzed+ char.upper()
        
        vivek = {'purpose':'Change to Uppercase','analyzed_text':analyzed}
        return render(request,'analyze.html',vivek)
    
    elif(newlineremover == "on"):
        analyzed=""
        for char in dj_text:
            if char != "\n":
                analyzed = analyzed + char

        vivek = {'purpose':'New line remover','analyzed_text':analyzed}
        return render(request,'analyze.html',vivek)
    
    elif(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(dj_text):
            #The enumerate function is used to get both the character (char) and its position (index) in the string.
            if index < len(dj_text) - 1 and dj_text[index] == " " and dj_text[index + 1] == " ":
                pass
            #This part checks if the current character (dj_text[index]) is a space and if the next character (dj_text[index + 1]) is also a space.
            # index < len(dj_text) - 1 ensures that we are not trying to access a character that doesn't exist
            # (i.e., it avoids going beyond the end of the string).
            else:
                analyzed = analyzed+ char

        vivek = {'purpose':'Extra space  remover','analyzed_text':analyzed}
        return render(request,'analyze.html',vivek)

    elif(charcount == "on"):
        count = 0
        for char in dj_text:
            
                if char!= " ":
                    count = count +1

        vivek = {'purpose':'Counting Characters','analyzed_text':count}
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






