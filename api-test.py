import requests
from pprint import pprint

quote_id = 3

content = requests.get('http://127.0.0.1:5000/api/quote/9')

pprint(content.json())