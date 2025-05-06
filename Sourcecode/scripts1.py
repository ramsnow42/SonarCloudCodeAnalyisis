import os
import requests
import sys

def trigger_workflow(token, owner, repo, workflow_name, parameter1=None, parameter2=None):
    """Trigger a GitHub Actions workflow using the GitHub API."""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {token}",
    }

    data = {
        "event_type": workflow_name,
        "client_payload": {
            "parameter1": parameter1,
            "parameter2": parameter2,
        },
    }

    url = f"https://api.github.com/repos/{owner}/{repo}/dispatches"
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 204:
        print(f"✅ Successfully triggered workflow: {workflow_name}")
    else:
        print(f"❌ Failed to trigger workflow. Status code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts1.py <TOKEN> <OWNER> <REPO> <WORKFLOW_NAME> [PARAMETER1] [PARAMETER2]")
        sys.exit(1)

    TOKEN = sys.argv[1]
    OWNER = sys.argv[2]
    REPO = sys.argv[3]
    WORKFLOW_NAME = sys.argv[4]
    PARAMETER1 = sys.argv[5] if len(sys.argv) > 5 else None
    PARAMETER2 = sys.argv[6] if len(sys.argv) > 6 else None

    trigger_workflow(TOKEN, OWNER, REPO, WORKFLOW_NAME, PARAMETER1, PARAMETER2)