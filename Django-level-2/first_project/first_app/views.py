from django.shortcuts import render

# Create your views here.


def index(requests):
    context = {
        'insert_me' : "I am from first_app"
    }
    return render(requests,'first_app/index.html', context = context )

def help(requests):
    context = {
        'help_me' : "I need help"
    }
    return render(requests, 'first_app/help.html', context = context)
