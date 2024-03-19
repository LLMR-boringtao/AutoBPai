import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.group_chat import GroupChatAgent as Agent


@mark.group_chat
class ToolsTests:
    def test_tools_behaviours(self):
        request = """Find the best platform to build LLM applications."""
        context = """"""
        agent_instance = Agent(request, context)
        result = agent_instance.actor()
        print("Result: ", result)
        assert result is not None