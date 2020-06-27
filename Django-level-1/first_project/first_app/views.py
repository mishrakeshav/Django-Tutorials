from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    context = {
        "insert_me": "This is the dynamic element",
    }
    return render(request,'first_app/index.html',context=context )

def help(request):
    context = {
        "insert_me": "This is the Help Page",
    }
    return render(request,'first_app/help.html',context=context )
