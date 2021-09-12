import os
import sublime
import importlib

from . import unittest
plugin = importlib.import_module("sublime-jester.plugin")


class TestGetJestExecutable(unittest.TestCase):

    def test_non_executable_raises_exeption(self):
        with self.assertRaises(ValueError):
            plugin._get_jest_executable(unittest.fixtures_path('foobar'))

    def test_found_executable(self):
        actual = plugin._get_jest_executable(unittest.fixtures_path('node_unix'))
        expected = os.path.join(unittest.fixtures_path(), 'node_unix', 'node_modules', '.bin', 'jest')
        self.assertEqual(actual, expected)

        actual = plugin._get_jest_executable(unittest.fixtures_path('node_win'))
        expected = os.path.join(unittest.fixtures_path(), 'node_win', 'node_modules', '.bin', 'jest.cmd')
        self.assertEqual(actual, expected)

