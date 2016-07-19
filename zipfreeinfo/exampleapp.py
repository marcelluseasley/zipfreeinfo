import zipfreeinfo


zipfreeinfo.set_auth_credentials('your auth id','your auth token')

# Returns a dictionary with nested data structures containing zip code data
# Also sets internal zipdata structure with zip code data, which can be returned with function calls
print(zipfreeinfo.get_zip_info("30141"))


print(zipfreeinfo.get_zipcode()) # returns string
print(zipfreeinfo.get_city()) # returns string
print(zipfreeinfo.get_state()) # returns string
print(zipfreeinfo.get_state_abbreviation()) # returns string
print(zipfreeinfo.get_county_fips()) # returns string
print(zipfreeinfo.get_county_name()) # returns string
print(zipfreeinfo.get_latitude()) # returns float
print(zipfreeinfo.get_longitude()) # returns float
