from app.envs.connector import Connector
connector = Connector()
kernel = connector.connect_azure_sk()

import os
from pathlib import Path

llm_config = {
    "type": "azure",
    "azure_deployment": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    "azure_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
}

work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)

class Agent:
    def __init__(self, request, context=""):
        self.request = request
        self.context = context

    def perceiver(self):
        query_request = self.request
        query_context = self.context
        query = str(query_request + " " + query_context)
        return query

    def planner(self):
        pass

    def actor(self):
        query = self.perceiver()

        return query