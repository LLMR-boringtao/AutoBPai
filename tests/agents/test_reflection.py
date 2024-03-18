import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.reflection import ReflectionAgent as Agent


@mark.reflection
class ReflectionTests:
    def test_reflection_behaviours(self):
        request = """What date is today? Compare the year-to-date gain for META and TESLA."""
        context = """"""
        agent_instance = Agent(request, context)
        result = agent_instance.actor()
        print(result)
        assert result is not None