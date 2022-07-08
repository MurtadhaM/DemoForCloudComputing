#!/usr/local/opt/python@3/bin/python3


from google.cloud import bigquery
from google_auth_oauthlib import flow
from google.oauth2 import service_account

launch_browser = True




client = bigquery.Client(project=project, credentials=credentials)

flow.run_console()

credentials = appflow.credentials
print(credentials)


client = bigquery.Client()
def implicit():
    from google.cloud import bigquery
    client = bigquery.Client()
    query = list(client.list_datasets())
    print(query)
client = bigquery.Client()


