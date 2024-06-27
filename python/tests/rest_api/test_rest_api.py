import json
import os

from tempfile import TemporaryDirectory
from click.testing import CliRunner
from typing import Tuple
from unittest import TestCase
from pydantic import BaseModel, FilePath

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from http import HTTPStatus

from aac.in_out.files.aac_file import AaCFile
from aac.in_out.parser._parser_error import ParserError
from aac.execute.aac_execution_result import ExecutionStatus
from aac.execute.command_line import cli, initialize_cli
from aac.in_out.parser._parse_source import parse
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

class TestRestApiCommands(TestCase):
    test_client = TestClient(app)

    def test_get_available_commands(self):
        response = self.test_client.get("/commands")
        self.assertEqual(HTTPStatus.OK, response.status_code)

    def test_execute_check_command(self):
        command_name = "check"
        test_model = parse(TEST_MODEL)[0]

        request_arguments = CommandRequestModel(name=command_name, arguments=[TEST_MODEL, "False", "False"])
        response = self.test_client.post("/command", data=json.dumps(jsonable_encoder(request_arguments)))

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertTrue(response.json().get("success"))
        self.assertIn("success", response.text)
        self.assertIn(command_name, response.text)
        self.assertIn(test_model.name, response.text)

    def test_execute_puml_component_command(self):
        command_name = "gen-plugin"
        test_model = parse(TEST_MODEL)[0]

        with TemporaryDirectory() as temp_dir:
            request_arguments = CommandRequestModel(name=command_name, arguments=[TEST_MODEL, temp_dir, temp_dir, temp_dir, "True", "True", "False"])
            response = self.test_client.post("/command", data=json.dumps(jsonable_encoder(request_arguments)))

            self.assertEqual(HTTPStatus.OK, response.status_code)
            self.assertTrue(response.json().get("success"))
            self.assertIn("success", response.text)
            self.assertIn(command_name, response.text)

    def test_execute_check_command_fails(self):
        command_name = "check"
        with self.assertRaises(Exception) as context:
            request_arguments = CommandRequestModel(name=command_name, arguments=[BAD_TEST_MODEL, "False", "False"])
            response = self.test_client.post("/command", data=json.dumps(jsonable_encoder(request_arguments)))


class TestAacRestApiFiles(TestCase):
    test_client = TestClient(app)

    def test_post_and_get_files(self):
        filepath = "tests/calc/model/calculator.yaml"
        self.assertTrue(os.path.isfile(filepath))

        file_model = FilePathModel(uri=filepath)
        self.test_client.post("/files/import", data=[file_model])
        response = self.test_client.get("/files/context")
        print(response.text)
        self.assertEqual(response)

    # def test_get_available_aac_files(self):
    #     test_model_definition


# class TestAacRestApiDefinitionEndpoints(ActiveContextTestCase):
#     test_client = TestClient(app)

#     def test_get_definitions(self):
#         self.maxDiff = None

TEST_MODEL = """
model:
    name: TestModel
    description: A TestModel
"""

BAD_TEST_MODEL = """
model:
    description: A TestModel
"""
