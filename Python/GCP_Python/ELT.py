
from http import client
from requests import options
from sympy import im


import google.cloud.bigquery as bigquery
from google.cloud import bigquery
import google.cloud.storage  as storage
import google.auth


credentials, project_id = google.auth.default()




class ELT(object):
    """_summary_
    This class is used to create an ELT object.
    1. Extract Data
    2. Load Data
    3. Transform Data
    """
    def __init__(self, data):
        self.data = data
        

    def extract_data(self):

        return self.data

    def load_data(self):

        return self.data

    def transform_data(self):

        return self.data



