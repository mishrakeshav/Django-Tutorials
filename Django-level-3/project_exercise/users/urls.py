
from django.urls import path 
from users import views

urlpatterns = [
    path('signup', views.users, name = 'signup'),
    path('', views.index, name = 'index'),
    
]