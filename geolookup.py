import json
import requests
import urllib.parse
import urllib.request


access_token = 'something-something-get-your-own-access-token-from-mapbox.com'


def lookup(address):
	'''Given an address, return latitude,longitude. Uses the mapbox API.'''
	address = urllib.parse.quote_plus(address)
	url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/%s.json?access_token=%s' % (address, access_token)
	r = requests.get(url, proxies=urllib.request.getproxies())
	body = r.text.replace('©','(c)')
	r = json.loads(body)
	if 'features' not in r or not r['features']:
		return None,None
	lng,lat = r['features'][0]['center']
	return lat,lng
