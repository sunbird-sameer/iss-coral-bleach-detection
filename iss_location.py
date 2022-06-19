import urllib.request
import json

obj = json.loads(urllib.request.urlopen('http://api.open-notify.org/iss-now.json').read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']

def lat():
    return str(lat)
def long():
    return str(long)

if __name__ == 'main':
    print("Latitude: " + lat)
    print("Longitude: " + long)
