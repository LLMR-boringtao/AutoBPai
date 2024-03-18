import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.bing import BingAgent as Agent


@mark.bing
class BingAgentTests:
    def test_bing_agent_behaviours(self):
        request = """如何可以帮忙开票"""
        context = """"""
        agent_instance = Agent(request, context)
        result = agent_instance.actor()
        print(result)
        assert result is not None