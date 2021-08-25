import requests
from pprint import pprint

url = "http://localhost:9200/products"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

pprint(response.text)
