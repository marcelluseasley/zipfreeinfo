# -*- coding: utf-8 -*-
import requests
import json
import collections

api_return_codes = {401: "Unauthorized", 402: "Payment Required", 413: "Request Entity Too Large",
                    400: "Bad Request (Malformed Payload)", 429: "Too Many Requests", 200: "OK"}

#credentials for smartystreets.com API
AUTH_ID = ''
AUTH_TOKEN = ''

ZIP_LOOKUP_URL = 'https://us-zipcode.api.smartystreets.com/lookup?auth-id={}&auth-token={}&zipcode={}'


zipdata = collections.defaultdict(str)

def set_auth_credentials(auth_id=None, auth_token=None):
    if auth_id is not None and auth_token is not None:
        AUTH_ID = auth_id
        AUTH_TOKEN = auth_token
        return 0
    return -1

def get_zip_info(zip_code=None):

    if zip_code is None:
        return -1

    if AUTH_ID is None or AUTH_TOKEN is None:
        return -1

    resp = requests.get(ZIP_LOOKUP_URL.format(AUTH_ID, AUTH_TOKEN, zip_code))

    if resp.status_code is not 200:
        return api_return_codes[resp.status_code]

    zipinfo = resp.json()




    zipdata['zip_code'] = zip_code
    zipdata['city'] = zipinfo[0]['city_states'][0]['city']
    zipdata['state_abbreviation'] = zipinfo[0]['city_states'][0]['state_abbreviation']
    zipdata['county_fips'] = zipinfo[0]['zipcodes'][0]['county_fips']
    zipdata['county_name'] = zipinfo[0]['zipcodes'][0]['county_name']
    zipdata['longitude'] = zipinfo[0]['zipcodes'][0]['longitude']
    zipdata['latitude'] = zipinfo[0]['zipcodes'][0]['latitude']
    zipdata['state'] = zipinfo[0]['city_states'][0]['state']

    return zipdata



def get_zipcode():
    return zipdata['zip_code']

def get_city():
    return zipdata['city']

def get_state():
    return zipdata['state']

def get_state_abbreviation():
    return zipdata['state_abbreviation']

def get_county_fips():
    return zipdata['county_fips']

def get_county_name():
    return zipdata['county_name']

def get_longitutde():
    return zipdata['longitude']

def get_latitude():
    return zipdata['latitude']


