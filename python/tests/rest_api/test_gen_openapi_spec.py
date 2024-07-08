import json
import os

from tempfile import TemporaryDirectory
from unittest import TestCase

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from http import HTTPStatus

from aac.context.constants import DEFINITION_FIELD_NAME
from aac.in_out.parser._parse_source import parse
from rest_api.models.command_model import CommandRequestModel
from rest_api.models.definition_model import to_definition_model
from rest_api.models.file_model import FilePathModel, FilePathRenameModel
from rest_api.aac_rest_app import app, refresh_available_files_in_workspace


class TestGenOpenApiSpec(TestCase):

    def test_gen_openapi_spec(self):
        # Like in core going to rely on the CLI testing for this, have not determined what we would like to test here
        pass

    def run_gen_openapi_spec_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["gen-openapi-spec"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message


    def test_cli_gen_openapi_spec_success(self):
        """Test the puml-component CLI command success for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            args = [temp_dir]
            exit_code, output_message = self.run_gen_openapi_spec_cli_command_with_args(args)

            temp_dir_files = listdir(temp_dir)
            self.assertNotEqual(0, len(temp_dir_files))
