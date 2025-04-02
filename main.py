import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# User Variables
USER_TOKEN = os.getenv("USER_TOKEN")
USER_NAME = os.getenv("USER_NAME")
GRAPH_ID = os.getenv("GRAPH_ID")

# Endpoints
endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{endpoint}/{USER_NAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Headers
headers = {"X-USER-TOKEN": USER_TOKEN}

# Create user if it does not exist
if requests.get(url=f"{endpoint}/{USER_NAME}").status_code != 200:
    requests.post(url=endpoint, json={
        "token": USER_TOKEN,
        "username": USER_NAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    })

# Create graph if it does not exist
graph_list = requests.get(url=graph_endpoint, headers=headers).json()
existing_graphs = {graph["id"] for graph in graph_list.get("graphs", [])}

if GRAPH_ID not in existing_graphs:
    requests.post(url=graph_endpoint, json={
        "id": GRAPH_ID,
        "name": "Meditation Graph",
        "unit": "Minutes",
        "type": "int",
        "color": "ajisai",
    }, headers=headers)

# Add pixel (activity)
requests.post(url=pixel_endpoint, json={
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "10",
}, headers=headers)