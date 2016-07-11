import django
import os
import sys
from scrape_site import *
from update_db import *
from send_emails import *
# Django settings config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()
from web_scraper.settings import BASE_DIR
from polls.models import Polls
#
json_file = os.path.join(BASE_DIR, 'latest_updates.json')
website = r'https://www.digitalmarketplace.service.gov.uk/digital-outcomes-and-specialists/opportunities'
website_ele = 'div'
website_tag = 'search-result'
scraped_info = get_information(raw_data=scrape_website(weburl=website, element=website_ele, tag=website_tag))
current_db = [r.title for r in Polls.objects.all()]
#from django.core.mail import send_mail
#send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
# Next steps for new record:

def run_program():
    new_entries = get_new_entries(current_data=current_db, scraped_data=scraped_info)
    if len(new_entries) >= 1:
        if update_database(new_entries=new_entries):
            # update trello
            # if update_trello
            send_emails(new_entries=new_entries, mailing_list=None)


run_program()
