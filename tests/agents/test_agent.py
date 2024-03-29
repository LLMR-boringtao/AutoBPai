import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.agent import Agent as Agent


@mark.agent
class AgentTests:
    def test_agent_behaviours(self):
        request = """如何登陆开票系统"""
        context = """"""
        agent_instance = Agent(request, context)
        result = agent_instance.actor()
        print(result)
        assert result is not None