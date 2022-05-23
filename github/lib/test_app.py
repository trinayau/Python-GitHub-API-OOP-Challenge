import pytest
import requests
from unittest import mock

from .api import fetch_repos
from .repository import Repository
from .app import CLI

class TestAPICase():
    def test_fetch_repos(self, repo_test_list):
        mock_response = mock.Mock()
        mock_response.json.return_value = repo_test_list

        mock_requests_get = mock.Mock(return_value=mock_response)

        requests.get = mock_requests_get
        fetch_repos()
        mock_requests_get.assert_called_with('https://api.github.com/users/')


class TestCLICase():
    @pytest.mark.parametrize('input, expected', [("1", True), ("0", False), ("4", False), ("3", True)])
    def test_valid_input(self, input, expected, monkeypatch):
        monkeypatch.setattr(Repository, "all", [{}, {}, {}])
        assert CLI.valid_input(input) == expected

    def test_goodbye(self, capsys):
        CLI.goodbye()
        out, err = capsys.readouterr()
        assert "Thanks for using my GitHub bot!" in out

    def test_show_repo(self, capsys, repo_test_data):
        self._original_find_by_input = Repository.find_by_input
        mock_find_by_input = mock.Mock(return_value=Repository(repo_test_data))
        Repository.find_by_input = mock_find_by_input

        CLI().show_repo()
        Repository.find_by_input = self._original_find_by_input

        mock_find_by_input.assert_called()
        out, err = capsys.readouterr()
        assert repo_test_data['name'] in out
