
import os
import autogen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json


config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST",
    filter_dict={
        "model": {
            "gpt-4"
        },
    }
)


assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

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