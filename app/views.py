from django.shortcuts import render, redirect
import time
from django.http import HttpResponse
import random

# Create your views here.
a = 0
tries = 0

def start(request):
    global a
    a = random.randint(1,100)
    global ōtries
    tries = 0
    begin = 'the random number has been generated!'
    content = {"begin" : begin}
    return render(request, 'index.html', content)
    


def index(request):
    message = ""
    again = ""
    congrats = ""
    tried = ""
    global tries
    x = globals() ['a']
    
    if request.method == "POST":
        var = int(request.POST.get('ans'))
        tries = tries + 1
        if x>var:
            message = "number is greater than your answer"
        
        elif x<var:
            message = "number is smaller than your answer"

        else:
            message = "Your answer is right " + str(x)
            congrats = "😎  ☆*: .｡. o(≧▽≦)o .｡.:*☆"
            tried = "you have tried " + str(tries) + " times so your score is 100-" + str(tries*5) + " = " + str(100-(tries*5))
            again = "if you want to play again press 'start'"
        
        if(tries>0):
            tried_1 = "you have tried " + str(tries) + " attempts"
    context = {"message" : message, "congrats" : congrats, "again" : again, "tried" : tried, "tries" : tried_1}

    return render(request, 'index.html', context)
 