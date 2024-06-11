from click.testing import CliRunner
from typing import Tuple
from unittest import TestCase

from aac.execute.aac_execution_result import ExecutionStatus
from aac.execute.command_line import cli, initialize_cli

from rest_api.rest_api_impl import plugin_name, rest_api, gen_openapi_spec


class TestRESTAPI(TestCase):

    def test_rest_api(self):

        # TODO: Write success and failure unit tests for rest_api
        self.fail("Test not yet implemented.")

    def run_rest_api_cli_command_with_args(self, args: list[str]) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["rest-api"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_rest_api(self):
        args = []

        # TODO: populate args list, or pass empty list for no args
        exit_code, output_message = self.run_rest_api_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

    def test_cli_rest_api_failure(self):
        args = []

        # TODO: populate args list, or pass empty list for no args
        exit_code, output_message = self.run_rest_api_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertNotEqual(
            0, exit_code
        )  # asserts the command did not run successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message contains correct failure message

    def test_gen_openapi_spec(self):

        # TODO: Write success and failure unit tests for gen_openapi_spec
        self.fail("Test not yet implemented.")

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

    def test_cli_gen_openapi_spec(self):
        args = []

        # TODO: populate args list, or pass empty list for no args
        exit_code, output_message = self.run_gen_openapi_spec_cli_command_with_args(
            args
        )

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

    def test_cli_gen_openapi_spec_failure(self):
        args = []

        # TODO: populate args list, or pass empty list for no args
        exit_code, output_message = self.run_gen_openapi_spec_cli_command_with_args(
            args
        )

        # TODO:  perform assertions against the output message
        self.assertNotEqual(
            0, exit_code
        )  # asserts the command did not run successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message contains correct failure message
