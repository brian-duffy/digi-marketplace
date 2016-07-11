import django
import os
import sys
# Django settings config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()
from web_scraper.settings import BASE_DIR
from polls.models import Polls
#

for doh in Polls.objects.all():
    try:
        print doh.location, doh.client, doh.title
    except:
        pass