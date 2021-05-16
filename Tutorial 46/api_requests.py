import requests
import json
url = "https://www.python.org/"
response = requests.get(url)
print(response.status_code)
if response:
    print("The page loaded")
else:
    print("Response failed")
#print(response.text)
json_element = json.dumps(response.text)
#print(json_element)
print(response.headers["Date"])