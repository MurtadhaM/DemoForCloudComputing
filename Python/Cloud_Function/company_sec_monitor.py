#!/usr/local/opt/python@3/bin/python3
import json
import sys
import requests
import json

# initial URL
url = "https://data.sec.gov/submissions/CIK0001758548.json"


# new  requests session
requests = requests.Session()


def download_json():
    try:
        requests.headers.update(
    {'User-Agent': 'Python Agent', "Accept-Encoding": "text,json"})
        data = requests.get(url).json()
        return data
    except:
        print("Error in getting the data")
        return None



def parse_information(json_data):
    urls = []
    try:
        documents = json_data['filings']['recent']['accessionNumber']
        document_names = json_data['filings']['recent']['primaryDocument']
        document_dates = json_data['filings']['recent']['filingDate']
        company_name = json_data['name']
        company_address = ""
        for value in (json_data['addresses']['mailing']).values():
            company_address += str(value) + " "
        company_address = str(company_address).strip()

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
        return (company_info)
    except:
        print("Error in getting the documents")
        return None

# main function
def __main__():
    JSON_DATA = parse_information(json_data=download_json())
    data = JSON_DATA.items()
    return JSON_DATA     

