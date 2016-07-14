import os
import sys
import django
from datetime import datetime
import lxml
import urllib2
import json
from bs4 import BeautifulSoup
# Django settings config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
django.setup()
from web_scraper.settings import BASE_DIR
#

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

def scrape_website(weburl=None, element=None, tag=None):
    website = weburl
    page = urllib2.urlopen(website)
    soup = BeautifulSoup(page, "lxml")
    all_results = soup.find_all(element, class_=tag)
    return all_results

def get_inner_information(raw_data=None):
    """
    Function will take an inner url and retrieve certain elements
    :param raw_data:
    :return:
    """
    print raw_data

def get_information(raw_data=None):
    # Takes array of search results and returns list [CLIENT, LOCATION, CLOSING_DATE, EXCERPT, URL_LINK, DATE_CLOSING]
    titles = [data.h2.text.replace('\n', '').lstrip() for data in raw_data]
    urls = [data.h2.a['href'] for data in raw_data]
    excerpts = [data.p.text.replace('\n', '').strip() for data in raw_data]
    raw_metadata = []
    metadata_objs = [raw.find_all('li', class_='search-result-metadata-item') for raw in raw_data]
    fields_l = []
    for i, meta in enumerate(metadata_objs):
        fields = {}
        columns={}
        if 'Closed' not in meta[3].text.replace('\n', '').lstrip():
            id = i + 1
            fields["model"] = 'polls.polls'
            fields["pk"] = id
            for x, data in enumerate(meta):
                # x[0] = Client
                # x[1] = Location
                # x[2] = ?
                # x[3] = Closing Date
                try:
                    if x ==0:
                        columns["client"] = meta[x].text.replace('\n', '').strip()
                    elif x == 1:
                        columns["location"] = meta[x].text.replace('\n', '').strip()
                    elif x == 2:
                        pass
                    elif x == 3:
                        columns["end_date"] = datetime.strptime(meta[3].text.replace('\n', '').strip()[9:], '%A %d %B %Y')
                except UnicodeEncodeError as e:
                    print 'Error: {}'.format(e.reason)
            columns["title"] = titles[i]
            columns["excerpt"] = excerpts[i]
            columns["url"] = urls[i]
            fields["fields"] = columns
            fields_l.append(fields)
    return fields_l
    #return json.dumps(fields_l, ensure_ascii=True, default=json_serial)
#website = r'https://www.digitalmarketplace.service.gov.uk/digital-outcomes-and-specialists/opportunities'
#website_ele = 'div'
#website_tag = 'search-result'
#
#print scrape_website(weburl=website, element=website_ele, tag=website_tag)[0]