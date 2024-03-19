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


assistant = autogen.AssistantAgent(
    name="assistant",
    system_message="For coding tasks, only use the functions you have been provided with. You have a stopwatch and a timer, these tools can and should be used in parallel. Reply TERMINATE when the task is done.",
    llm_config={
        "cache_seed": 41,  
        "config_list": config_list,  
        "temperature": 0, 
    },
)
user_proxy = autogen.UserProxyAgent(
    name = "user_proxy",
    system_message="A proxy for the user for executing code.",
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 2,
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config = {
        "work_dir": "app/code",
        "use_docker": False,
    },
)

@user_proxy.register_for_execution()
@assistant.register_for_llm(description="create a timer for N seconds")
async def timer(num_seconds: Annotated[str, "Number of seconds in the timer."]) -> str:
    for i in range(int(num_seconds)):
        time.sleep(1)
    return "Timer is done!"
autogen.agentchat.register_function(
    timer,
    caller=assistant,
    executor=user_proxy,
    description="create a timer for N seconds",
)


class ToolsAgent:
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
    
    async def actor(self):
        query = self.perceiver()

        result = ""
        with Cache.disk() as cache:
            chat_res = await user_proxy.a_initiate_chat(
                assistant,
                message=query,
                cache=cache,
            )
        result = chat_res.chat_history[-1]['content']    

        return result