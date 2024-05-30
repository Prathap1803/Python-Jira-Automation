# JIRA Issue Creation API

This Flask application provides an API endpoint to create JIRA issues based on received POST requests.

## Requirements

- Python 3.x
- Flask
- Requests

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/jira-issue-creator.git
   cd jira-issue-creator
2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. pip install -r requirements.txt
Configuration
Update the following variables in the createJira function with your own JIRA instance details:

`url`: The JIRA API endpoint for creating issues.
`API_TOKEN`: Your JIRA API token.
`auth`: Replace "dummy.dotx@gmail.com" with your JIRA username.

## Running the Application
  - To run the Flask application, use the following command:
    ```bash
    python app.py


By default, the application will run on http://0.0.0.0:8000.

## Setting Up GitHub Webhook
1. Navigate to your repository on GitHub.
2. Go to `Settings` > `Webhooks` > `Add webhook`.
3. Configure the webhook with the following settings:
    - Payload URL: http://your-server-ip:8000/createJira (replace your-server-ip with your actual server IP address)
    - Content type: `application/json`
    - Secret: (optional)
    - Events: Choose `Let me select individual events` and select the events you want to trigger the webhook, such as `Issues` or `Issue comments`.
## API Endpoint
**POST /createJira**
- This endpoint creates a JIRA issue if the comment body contains /jira.

**Request**:
- Method: `POST`
- URL: `/createJira`
- Headers:
    - Content-Type: `application/json`
- Body
    ```bash
    curl -X POST http://0.0.0.0:8000/createJira \
     -H "Content-Type: application/json" \
     -d '{
           "issue": {
             "title": "Sample Issue",
             "body": "This is a sample issue description"
           },
           "comment": {
             "body": "/jira"
           }
         }'

## Notes
- Ensure your JIRA API token and username are kept secure and not exposed in public repositories.
- The project key and issue type ID must be updated according to your JIRA instance.
