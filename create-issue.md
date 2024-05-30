# JIRA Issue Creation Script

This Python script allows you to create a JIRA issue using the JIRA REST API.

## Requirements

- Python 3.x
- Requests library

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/jira-issue-creator.git
   cd jira-issue-creator
2. **Create a virtual environment:**
     ```bash
     python3 -m venv venv
   source venv/bin/activate
3. **Install the required package:**
     ```bash
     pip install requests
## Configuration
Update the following variables in the script with your own JIRA instance details:
  - `url`: The JIRA API endpoint for creating issues.
  - `API_TOKEN`: Your JIRA API token.
  - `auth`: Replace "<your-jira-gmail>" with your JIRA username.
## Code Explanation
The script uses the requests library to send a POST request to the JIRA REST API to create a new issue. Below is a detailed explanation of the code:

1. **Imports**
    ```python
        import requests
        from requests.auth import HTTPBasicAuth
        import json

These imports are necessary for making HTTP requests and handling JSON data.
2.  **Configuration**
   ```python
    url = "https://<your-jira-domainlink>/rest/api/3/project"
  API_TOKEN = ""
  auth = HTTPBasicAuth("<your-jira-gmail>", API_TOKEN)

```
- url: The endpoint for creating JIRA issues. Replace <your-jira-domainlink> with your JIRA domain.
- API_TOKEN: Your JIRA API token. You need to generate this token from your JIRA account.
- auth: Basic authentication using your JIRA username and API token.

3. **Headers**
```python
headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
These headers specify that the request and response content will be in JSON format.

Payload
python
Copy code
payload = json.dumps({
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
    "summary": "Main order flow broken"
  },
  "update": {}
})
```
- `description`: The description of the issue, formatted in a way compatible with JIRA's content management.
- `issuetype`: The ID of the issue type. Replace 10019 with the appropriate issue type ID for your JIRA instance.
- `project`: The key of the project where the issue will be created. Replace "MD" with your project's key.
- `summary`: A brief summary of the issue.
- Sending the Request
```python
Copy code
response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)
```
This sends a POST request to the JIRA API with the specified URL, payload, headers, and authentication.

4. **Printing the Response**
```python

print(((response.text)))

```
This prints the response from the JIRA API, which will include details of the created issue or an error message if the request was unsuccessful.

**Running the Script**
To run the script, use the following command:

```bash

python create_jira_issue.py
```
Replace `create_jira_issue.py` with the filename of your script.

**Notes**
- Ensure your JIRA API token and username are kept secure and not exposed in public repositories.
- Update the project key and issue type ID according to your JIRA instance.
