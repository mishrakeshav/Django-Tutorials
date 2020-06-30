from django.shortcuts import render

# Create your views here.
from first_app.models import Topic, WebPage, AccessRecord

def index(requests):
    accessrecords = AccessRecord.objects.order_by('date')
    context = {
        'accessrecords' : accessrecords
    }
    return render(requests,'first_app/index.html', context = context )

def help(requests):
    context = {
        'help_me' : "I need help"
    }
    return render(requests, 'first_app/help.html', context = context)
