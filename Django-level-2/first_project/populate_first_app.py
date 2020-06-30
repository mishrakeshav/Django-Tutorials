import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

# Faker Pop script 
import random 
from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()

    return t

def populate(N=5):

    for entry in range(N):
        top = add_topic()

        # creating fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #creating a new webpage entry 
        webpg = WebPage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
        webpg.save()
        #create a fake access record for that webpage 
        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]
        acc_rec.save()

if __name__ == '__main__':
    print("Populating script.......")
    populate(20)
    print("populating completed !")

