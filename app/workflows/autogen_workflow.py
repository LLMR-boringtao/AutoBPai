import autogen
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")
llm_config = {
    "cache_seed": 42,
    "temperature": 0,
    "config_list": config_list,
    "timeout": 120,
}

extractor = autogen.AssistantAgent(
    name="Extractor",
    system_message="""提取发票类型/客户名称/商品序号/商品名称/商品规格型号/商品单位/商品数量/商品含税金额。商品序号自动从1开始递增。如有多个商品，每个商品列出相应的商品名称/商品规格型号/商品单位/商品数量/商品含税金额。""",
    llm_config=llm_config,
)

calculation = autogen.AssistantAgent(
    name="Calculation",
    system_message="根据提取的信息，计算发票总金额等于所有商品数量乘以商品含税金额的总和。",
    llm_config=llm_config,
)

accountant = autogen.UserProxyAgent(
    name="Accountant",
    system_message="将提取信息列出，提醒用户缺失的信息，回复`TERMINATE`结束对话",
    code_execution_config=False,
    human_input_mode="TERMINATE",
)

groupchat = autogen.GroupChat(agents=[extractor, calculation, accountant], messages=[], max_round=5)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

class AutoGenWorkflow:
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

        chat_res = accountant.initiate_chat(
            manager, 
            message=query
        )

        def get_contents(chat_result):
            contents = []
            for message in chat_result.chat_history:
                if 'name' in message and message['name'] in ['Extractor', 'Calculation']:
                    contents.append(message['content'])
            return '\n\n'.join(contents)

        result = get_contents(chat_res)

        return result