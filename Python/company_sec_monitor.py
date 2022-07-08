#!/usr/local/opt/python@3/bin/python3
import json
from fake_useragent import UserAgent

import requests


import json



urls = []


def get_info():
    try:
        data = requests.get(url).json()
        return data
    except:
        print("Error in getting the data")
        return None

requests = requests.Session()

requests.headers.update(
    {'User-Agent': 'Python Agent', "Accept-Encoding": "text,json"})
url = "https://data.sec.gov/submissions/CIK0001758548.json"
json_data = get_info()


def get_documents(json_data):
    try:
        documents = json_data['filings']['recent']['accessionNumber']
        document_names = json_data['filings']['recent']['primaryDocument']
        document_dates = json_data['filings']['recent']['filingDate']
        company_name = json_data['name']
        company_address = str(json_data['addresses']['mailing'])
        company_phone = str(json_data['phone'])
        last_updated = document_dates[0]


        for document in documents:
            document = document.replace("-", "")
            urls.append(
                f'https://www.sec.gov/Archives/edgar/data/0001758548/{document}/xslFormDX01/primary_doc.xml')
        company_info = {
            "company_name": company_name,
            "company_address": company_address,
            "company_phone": company_phone,
            "document_names": document_names,
            "document_dates": document_dates,
            "document_urls": urls,
            "last_updated": last_updated
        }
        return json.dumps(company_info)
    except:
        print("Error in getting the documents")
        return None


print(get_documents(json_data))

