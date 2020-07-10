import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_exercise.settings')

import django 
django.setup()

# Faker Pop script 
import random 
from users.models import User
from faker import Faker

fake_gen = Faker()

def add_user(N=5):
    for i in range(N):
        first_name= fake_gen.first_name()
        last_name = fake_gen.last_name()
        email = fake_gen.email()
        user = User.objects.get_or_create(first_name = first_name, last_name = last_name, email = email)[0]
        user.save()

if __name__ == '__main__':
    print("Populating users .....")
    add_user(20)
    print("populating completed!")