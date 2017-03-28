import requests
import json

def getDocs():
	url = "https://topics-e26e.restdb.io/rest/munca"

	headers = {
	    'content-type': "application/json",
	    'x-apikey': "8a598b90e251b3edaed8860761b4852a5cbd1",
	    'cache-control': "no-cache"
	    }

	response = requests.request("GET", url, headers=headers)

	print(response.text)
	                    

def postNewDoc():
	url = "https://topics-e26e.restdb.io/rest/munca"

	payload = json.dumps( {"field1": "xyz","field2": "abc"} )
	headers = {
	    'content-type': "application/json",
	    'x-apikey': "8a598b90e251b3edaed8860761b4852a5cbd1",
	    'cache-control': "no-cache"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)

getDocs()
# postNewDoc()