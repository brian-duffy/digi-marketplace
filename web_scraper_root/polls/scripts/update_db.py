import django
import os
import sys
from scrape_site import *
# Django settings config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()
from web_scraper.settings import BASE_DIR
from polls.models import Polls
#

def get_new_entries(current_data=None, scraped_data=None):
    return [n for n in scraped_data if n['fields']['title'] not in current_data]

def update_database(new_entries=None):
    return True

