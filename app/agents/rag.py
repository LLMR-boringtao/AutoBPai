import chromadb
import json
import os


import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from autogen.retrieve_utils import TEXT_FORMATS

from autogen import config_list_from_json
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")
print(TEXT_FORMATS)

class RAGAgent:
    def __init__(self, request, context=""):
        self.request = request
        self.context = context
        self.assistant = RetrieveAssistantAgent(
            name="rag_assistant",
            system_message="You are a helpful rag assistant.",
            llm_config={
                "timeout": 600,
                "cache_seed": 42,
                "config_list": config_list,
            },
        )
        self.ragproxyagent = RetrieveUserProxyAgent(
            name="ragproxyagent",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=3,
            retrieve_config={
                "task": "code",
                "docs_path": [
                    os.path.join(os.path.abspath(""), "app/data/测试税编码表.csv"),
                ],
                "custom_text_types": ["csv"],
                "chunk_token_size": 2000,
                "model": config_list[0]["model"],
                "client": chromadb.PersistentClient(path="/tmp/chromadb"),
                "embedding_model": "all-mpnet-base-v2",
                "get_or_create": True,
            },
            code_execution_config=False,
        )

    def perceiver(self):
        query_request = self.request
        query_context = self.context
        query = str(query_request + " " + query_context)
        return query

    def planner(self):
        pass

    def actor(self):
        query = self.perceiver()

        self.assistant.reset()
        qa_problem = query
        self.ragproxyagent.initiate_chat(
            self.assistant, message=self.ragproxyagent.message_generator, problem=qa_problem, search_string="增值税税率"
        )