
import json
from logging import Logger
from typing import Dict, Optional
import company_sec_monitor
from google.cloud import bigquery

# Variables TO BE CHANGED
dataset_id = "Company_Info"
table_id = "Summary_Info"
bigquery_client = bigquery.Client(project="wellnecitydemo")
# Schema for the table
TABLE_SCHEMA = f"""
    company_name STRING,
    company_address STRING,
    company_phone STRING,
    last_updated STRING,
    document_urls Array<STRING>,
    document_names Array<STRING>,
    """
    
    
def fetch_data():
    dict_data = company_sec_monitor.__main__()
    return dict_data

def create_dataset(dataset_id: str) -> None:
    dataset_id_full = "{}.{}".format(bigquery_client.project, dataset_id)
    # create a pointer to the dataset
    dataset = bigquery.Dataset(dataset_id_full)
    # create the dataset if it doesn't exist
    dataset = bigquery_client.create_dataset(dataset , exists_ok=True)
    print("Dataset created")
    return dataset

def create_table(dataset_name, table_name, schema="") -> None:
    table_id_full = "{}.{}.{}".format(bigquery_client.project, dataset_name, table_name)
    table = bigquery.Table(table_id_full)
    SQL_CREATE_TABLE = f"""
    CREATE TABLE IF NOT EXISTS `{table_id_full}`
    (
        {schema}
    );
    """
    log = bigquery_client.query(SQL_CREATE_TABLE)
    print("Table created")

def insert_data(dataset_name, table_name, data):
    table_id_full = "{}.{}.{}".format(bigquery_client.project, dataset_name, table_name)
    table = bigquery.Table(table_id_full)
    query = (
        f'insert into {table_id_full} values ({data}) '
    )
    log = bigquery_client.query(query)
    print("DATA INSERTED")
    
def data_prep(data):
    company_name =  data['company_name']
    company_address =  data['company_address']
    company_phone =  data['company_phone']
    last_updated =      data['last_updated']
    document_names =    data['document_names']
    document_dates =   data['document_dates']
    Documents = {"date": f'{data["document_dates"]}', "link": f'{data["document_urls"]}'}
    print("DATA PREPARED")
    return f'"{company_name}", "{company_address}", "{company_phone}", "{last_updated}", {document_names} , {document_dates}'


def execute_function(dataset_name, table_name) -> None:
    # dropping Dataset if it exists
    dataset = bigquery_client.dataset(dataset_name)
    bigquery_client.delete_dataset(dataset, delete_contents=True)
    # # Creates a dataset.
    print("Creating DATASET")
    create_dataset(dataset_name)
    print("CREATING TABLE")
    # # create the table if it doesn't exist
    create_table(dataset_name, table_name, TABLE_SCHEMA)
    # # Fetch the data from the API
    JSON_DATA = fetch_data()  
    print("PREPARING QUERY")
    PREPARED_DATA = data_prep(JSON_DATA)
    print("INSERTING DATA")
    insert_data(dataset_name, table_name,   PREPARED_DATA )
    
    
    


    
if __name__ == "__main__":
    # Execute the function
    execute_function(dataset_id, table_id)
   
