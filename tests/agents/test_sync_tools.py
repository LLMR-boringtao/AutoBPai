import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.sync_tools import ToolsAgent as Agent


@mark.tools
class ToolsTests:
    def test_tools_behaviours(self):
        request = """Create a timer for 1 seconds and then a stopwatch for 1 seconds."""
        context = """"""
        agent_instance = Agent(request, context)
        result = agent_instance.actor()
        print("Result: ", result)
        assert result is not None