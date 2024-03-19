import chromadb
import json
import os
import time


import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.cache import Cache
from typing_extensions import Annotated

from autogen import config_list_from_json
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")


llm_config = {"config_list": config_list, "cache_seed": 42}

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "groupchat",
        "use_docker": False,
    },
    human_input_mode="TERMINATE",
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)


class GroupChatAgent:
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

        result = ""
        chat_res = user_proxy.initiate_chat(
            manager, 
            message = query
        )

        def get_contents(chat_result):
            contents = []
            for message in chat_result.chat_history:
                if 'name' in message and message['name'] in ['Product_manager', 'Coder']:
                    contents.append(message['content'])
            return '\n\n'.join(contents)

        result = get_contents(chat_res)

        return result