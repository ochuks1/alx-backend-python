#!/usr/bin/env python3
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch.object(GithubOrgClient, 'org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        mock_org.return_value = org_payload
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, org_payload["repos_url"])

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        mock_repos_url.return_value = "test_url"
        mock_get_json.return_value = repos_payload
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), expected_repos)
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("test_url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)

@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        mock_get = cls.get_patcher.start()
        mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
