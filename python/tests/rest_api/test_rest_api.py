from click.testing import CliRunner
from typing import Tuple
from unittest import TestCase

from fastapi.testclient import TestClient

from aac.execute.aac_execution_result import ExecutionStatus
from aac.execute.command_line import cli, initialize_cli
from rest_api.rest_api_impl import plugin_name, rest_api, gen_openapi_spec
from rest_api.models.command_model import (
    CommandModel,
    CommandRequestModel,
    CommandResponseModel,
    to_command_model,
)
from rest_api.models.definition_model import DefinitionModel, to_definition_class, to_definition_model
from rest_api.models.file_model import FileModel, FilePathModel, FilePathRenameModel, to_file_model
from rest_api.aac_rest_app import app, refresh_available_files_in_workspace

class TestRestAPI(TestCase):

    test_client = TestClient(app)
    def test_get_available_commands(self):
        response = self.test_client.get("/commands")
        print(response)


