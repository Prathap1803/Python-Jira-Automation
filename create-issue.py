import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://<your-jira-domainlink>/rest/api/3/project"

API_TOKEN = ""
auth = HTTPBasicAuth("<your-jira-gmail>", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
  
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Demo first JIRA ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    
    
    
    "issuetype": {
      "id": "10019"
    },
    
    "project": {
      "key": "MD"
    },
    
    "summary": "Main order flow broken",
    
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(((response.text) ))