
import os
import autogen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from autogen import ConversableAgent


config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

agent_accountant = ConversableAgent(
    "accountant",
    system_message="你是一个会计。你对开票操作系统没有了解。",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER"
)

agent_engineer = ConversableAgent(
    "engineer",
    system_message="你是一个工程师。你对开票操作系统非常了解。",
    llm_config={"config_list": config_list},
    human_input_mode="NEVER"
)


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
        result = agent_accountant.initiate_chat(agent_engineer, message=query, max_turns=2)

        return result