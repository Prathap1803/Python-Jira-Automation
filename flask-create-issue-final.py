from requests.auth import HTTPBasicAuth
import json
import requests
from flask import Flask, request
app = Flask(__name__)

@app.route("/createJira",methods=['POST'])
def createJira():

    url = "https://dummy-dot5.atlassian.net/rest/api/3/issue"
    API_TOKEN="ATATT3xFfGF0dopb7ec9MZxlHoChjSsz_2_QkKQWDpyVUIqugdmBsJJ2bq9dRJaUeGdBy8vQs-_G_Q71d2QX9yTY1G2z9LzaDevNyHW-doC6XiWuD0l5ZJxMWcy9VDGKMuYN8diCjMdmjousv_kl4moVV8ypDYfIDXK80EvbK41hh7uUkO_ViAI=C4D8F694"
    data1 = json.loads(request.data)
    
    auth = HTTPBasicAuth("dummy.dotx@gmail.com", API_TOKEN)
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
                "text": (data1["issue"]["body"]),
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
        "id": "10015"
        },
        "project": {
        "key": "DEMO"
        },
        "summary": (data1["issue"]["title"]),
    },
    "update": {}
    
    })
    data1 = json.loads(request.data)

    if ((data1["comment"]["body"])=="/jira") :
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
    else:
        print ("Please enter valid comments  : ")

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
