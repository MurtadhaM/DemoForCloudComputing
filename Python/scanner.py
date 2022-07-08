#!/usr/local/opt/python@3/bin/python3

from base64 import encode
from requests import request
import requests
from fake_useragent import UserAgent

headers = []

def randomAgent():
    random_user_agent = UserAgent().random.split('\n')[0]
    return {'User-Agent': random_user_agent}


def reverse_ip_lookup(host):
    try:
        res = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={host}', headers=randomAgent())
        headers.append({host: res.text})
    except:
        print("Error in getting the headers")
        return None
    return res.text


def http_header_scanner(host):

    try:
        
        res = requests.get(f'https://api.hackertarget.com/httpheaders/?q={host}', headers=randomAgent())
        headers.append({host: res.text})
    except:
        print("Error in getting the headers")
        return None
    return res.text
http_header_scanner("https://wellnecity.com")
reverse_ip_lookup("104.207.254.13")
print(headers)

