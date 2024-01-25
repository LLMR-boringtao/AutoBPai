from app.env.connect import Connector
connector = Connector()
kernel = connector.connect_azure_sk_embedding()

import os
from collections import defaultdict

bing_api_key = os.getenv("BING_API_KEY")

llm_config = {
    "type": "azure",
    "azure_deployment": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    "azure_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
    "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
}

from app.skills.Autogen.sk_bing_plugin import BingPlugin
from app.skills.Autogen.sk_web_pages_plugin import WebPagesPlugin
from app.skills.Autogen.autogen_plugin import AutoGenPlanner
class BingAgent:
    def __init__(self, request, context=""):
        self.request = request
        self.context = context

    def perceiver(self):
        query_request = self.request
        query_context = self.context
        query = str(query_request + " " + query_context)
        return query
    
    def planner(self):
        kernel.import_skill(BingPlugin(bing_api_key))
        kernel.import_skill(WebPagesPlugin())
        planner = AutoGenPlanner(kernel, llm_config)
        return planner
    
    def actor(self):
        query = self.perceiver()
        planner = self.planner()
        assistant = planner.create_assistant_agent("Assistant")
        worker = planner.create_user_agent("Worker", max_auto_reply=2, human_input="NEVER")
        worker.initiate_chat(assistant, message=query)
        
        data = defaultdict(list, worker.chat_messages)
        agent_key = [key for key in data.keys()][0]

        result = ""
        for item in data[agent_key]:
            if item['role'] == 'user':
                if item['content'] == 'TERMINATE':
                    pass
                else:
                    result = result + item["content"]

        return result

    def rlhf(self):
        pass