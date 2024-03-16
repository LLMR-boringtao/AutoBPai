import warnings
warnings.filterwarnings("ignore")

from pytest import mark
from app.envs.connector import Connector


@mark.env
class ConnectorTests:
    def test_connector_object_exists(self):
        connector = Connector()
        assert connector is not None

    def test_azure_sk(self):
        connector = Connector()
        kernel = connector.connect_azure_sk()
        assert kernel is not None

  
    
    