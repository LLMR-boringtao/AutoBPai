import chromadb
import json
import os


import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.retrieve_utils import TEXT_FORMATS

from autogen import config_list_from_json
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")


class ReflectionAgent:
    def __init__(self, request, context=""):
        self.request = request
        self.context = context
        self.assistant = autogen.AssistantAgent(
            name="assistant",
            llm_config={
                "cache_seed": 41,  
                "config_list": config_list,  
                "temperature": 0, 
            },
        )
        self.user_proxy = autogen.UserProxyAgent(
            name = "user_proxy",
            human_input_mode = "NEVER",
            max_consecutive_auto_reply = 10,
            is_termination_msg = lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config = {
                "work_dir": "app/data",
                "use_docker": False,
            },
        )

    def perceiver(self):
        query_request = self.request
        query_context = self.context
        query = str(query_request + " " + query_context)
        return query

    def planner(self):
        pass

    def _message_generator(self, sender, recipient, context):
        file_name = context.get("file_name")
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                file_content = file.read()
        except FileNotFoundError:
            file_content = "No data found."
        return "Write a brief summary about which company is doing better and explain why. \n Data: \n" + file_content
    
    def actor(self):
        query = self.perceiver()

        self.assistant.reset()
        chat_res = self.user_proxy.initiate_chat(
            self.assistant,
            message = self._message_generator,
            file_name = "app/data/stock_price.csv",
            summary_method = "reflection_with_llm"
        )

        result = chat_res.summary
        return result