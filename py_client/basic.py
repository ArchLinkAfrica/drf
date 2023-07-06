import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"hello archlinkafrica"}) # http request
print(get_response.text) # print raw text response


# HTTP  request -> html
# REST API HTTP request -> JSON
# Javascript object nototion ~ python dict
print(get_response.JSON())
print(get_response.status.code)

