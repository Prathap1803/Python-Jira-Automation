# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://dummydotx.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0DnVsEpZmlqx5S2zgOJsax1wcX1qyOGwoFt5GsrYIiAtSC6EJHWjjbfMyAOM6CMfh6_a5LgW3wf4uPlEDeY_Iel9Tojxyv5hznJV2COjo0HOOht3b_KoKIQG7N8usXSXiYIdHreIJa-9AlUcJmKfrjGvIWnLx3nFJdAneUK5MF4Y=5981BF7E"
auth = HTTPBasicAuth("dummy.dotx@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
print (type(output))
for i in range (len(output)):
    print(output[i]["name"])