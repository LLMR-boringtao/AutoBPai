import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.tools_async import ToolsAgent as Agent


@mark.asyncio
@mark.tools_async
class ToolsTests:
    async def test_tools_behaviours(self):
        request = """Create a timer for 1 seconds"""
        context = """"""
        agent_instance = Agent(request, context)
        result = await agent_instance.actor()
        print("Result: ", result)
        assert result is not None