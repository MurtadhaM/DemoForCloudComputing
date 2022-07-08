#!/usr/local/opt/python@3/bin/python3
import functions_framework
from google.cloud import bigquery
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


def get_documents(json_data):
    try:
        documents = json_data['filings']['recent']['accessionNumber']
        document_names = json_data['filings']['recent']['primaryDocument']
        document_dates = json_data['filings']['recent']['filingDate']
        company_name = json_data['name']
        company_address = ""
        for value in (json_data['addresses']['mailing']).values():
            company_address += str(value) + " "
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
        return company_info
    except:
        print("Error in getting the documents")
        return None


    
    


@functions_framework.http
def update_info(request):

    json_data = get_info()
    company_info = get_documents(json_data)

    table_name = "protean-sensor-355503.SEC_Filings.Fillings"
    company_name = company_info['company_name']
    company_address = (company_info['company_address'])
    company_phone = company_info['company_phone']
    last_updated = company_info['last_updated']
    document_names = json_data['filings']['recent']['primaryDocument']
    document_dates = json_data['filings']['recent']['filingDate']
    Documents = {"date": f'{document_dates}', "link": f'{urls}'}
    print(company_info)
    client = bigquery.Client()
    query = (
        f'insert into {table_name} values ("{company_name}","{company_address}","{company_phone}","{last_updated}",(select ("{str(Documents["date"])}" ,"{str(Documents["link"])}"))) '
    )

    query_job = client.query(
        query,
        location="us-east4"
    )
    results = query_job.result()
    print("Got {} rows.".format(results.total_rows))
