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
    """sets the auth_id and auth_token globally"""
    if auth_id is not None and auth_token is not None:
        global AUTH_ID
        global AUTH_TOKEN
        AUTH_ID = auth_id
        AUTH_TOKEN = auth_token
        return 0
    print("Function takes two arguments, auth_id and auth_token as strings")
    return None

def get_zip_info(zip_code=None):
    """given a zip code, it returns a json dictionary object with nested data"""
    if zip_code is None:
        print("Function takes zip_code as a string")
        return None

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
    """returns the zip code as a string"""
    return zipdata['zip_code']

def get_city():
    """returns the city"""
    return zipdata['city']

def get_state():
    """returns the state"""
    return zipdata['state']

def get_state_abbreviation():
    """returns the abbreviated state"""
    return zipdata['state_abbreviation']

def get_county_fips():
    """returns the five-digit Federal Information Processing Standard (FIPS) code"""
    return zipdata['county_fips']

def get_county_name():
    """returns the county name"""
    return zipdata['county_name']

def get_longitude():
    """returns the longitude as a float"""
    return zipdata['longitude']

def get_latitude():
    """returns the latitude as a float"""
    return zipdata['latitude']


