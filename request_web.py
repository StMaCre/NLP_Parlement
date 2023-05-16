import requests

url = 'https://www.pfwb.be/documents-parlementaires'

response = requests.get(url)

print(response.content)
