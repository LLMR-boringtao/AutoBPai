import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.agents.rag import RAGAgent as Agent


@mark.rag
class RAGTests:
    def test_rag_behaviours(self):
        request = """滑石的税率是多少?"""
        context = """"""
        agent_instance = Agent(request, context)
        agent_instance.actor()