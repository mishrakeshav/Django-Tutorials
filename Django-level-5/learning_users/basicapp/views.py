from django.shortcuts import render
from django.contrib.auth.models import User
from basicapp.forms import UserForm, UserProfileInfoForm


# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #saving the user to the model
            user = user_form.save()

            #hashing the password and then saving that to the database
            user.set_password(user.password)
            user.save()

            #we pass commit = False to avoid collision
            profile = profile_form.save(commit = False)
            #this maintains the onetoone relationship with the user
            
            #check if the user has uploded a file
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            #save the model
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(
        request, 

        'basicapp/registration.html',

        {'user_form':user_form,
        'profile_form':profile_form,
        'registered':registered
        }
    )