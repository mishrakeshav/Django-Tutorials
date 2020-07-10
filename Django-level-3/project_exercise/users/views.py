from django.shortcuts import render
# from users.models import User

from users.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def users(request):

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error! form in valid")
    return render(request, 'users/users.html', {'form':form})
