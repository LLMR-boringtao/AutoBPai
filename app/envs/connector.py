import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureTextEmbedding
from semantic_kernel.connectors.search_engine import BingConnector
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

class Connector:
    def __init__(self):
        pass

    def connect_azure_sk(self):
        kernel = sk.Kernel()
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        service_id = "default"
        kernel.add_service(
            AzureChatCompletion(service_id=service_id, deployment_name=deployment, endpoint=endpoint, api_key=api_key),
        )
        
        return kernel
    
    def connect_azure_bing(self):
        bing_api_key = os.getenv('BING_API_KEY')
        client = BingConnector(api_key=bing_api_key)

        return client