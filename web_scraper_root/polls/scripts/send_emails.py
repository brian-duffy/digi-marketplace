import django
import os
import sys
from scrape_site import *
from update_db import *
# Django settings config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()
from django.core.mail import EmailMultiAlternatives
#


def send_emails(mailing_list=None, new_entries=None):
    for entry in new_entries:
        email_subject, email_txt_body, email_html_body = compose_email(entry=entry)
        msg = EmailMultiAlternatives(email_subject, email_txt_body, 'Digital MarketPlace Unofficial Newsletter',
                                     ['brian.duffy@soprasteria.com'])
        msg.attach_alternative(email_html_body, "text/html")
        msg.send()

def compose_email(entry=None):
    """
    Composes an email subject and body
    :param new_entry:
    :return:
    """
    title = entry['fields']['title']
    end_date = entry['fields']['end_date']
    url = 'https://www.digitalmarketplace.service.gov.uk{}'.format(entry['fields']['url'])
    body = entry['fields']['excerpt']
    client = entry['fields']['client']
    location = entry['fields']['location']
    email_subject = 'New Opportunity With {} in {}'.format(client,location)
    email_txt_body = """
    {} is looking for {} in {}.
    More information: {}
    End date for bid: {}
    Link to post: {}
    """.format(client, title, location, body, end_date, url)
    email_html_body = """
        <h1><p><b>{}</b> is looking for {} in {}.</p><h1>
        <h2><p>More information: {}</p>
        <p>End date for bid: {}</p>
        <p>Link to post <a href=\"{}\"> <b>here</b></a></p></h2>
        """.format(client, title, location, body, end_date, url)
    return email_subject, email_txt_body, email_html_body


