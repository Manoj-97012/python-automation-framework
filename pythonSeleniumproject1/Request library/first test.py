import requests
import json

response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
print(response.text)
dict_response = json.loads(response.text)
print(dict_response)
dict_1 = dict_response[0]
print(dict_1['id'])

print(dict_1['name'])
print(dict_1['photo'])
for dict_2 in dict_1:
    print(dict_2)
