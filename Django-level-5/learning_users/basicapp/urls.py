from django.urls import path
from basicapp import views

#Template tagging
app_name = 'basicapp'


urlpatterns = [
    path('register/', views.register, name = 'register') , 
]

