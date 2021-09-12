import importlib
import os
from . import unittest
plugin = importlib.import_module("sublime-jester.plugin")


class TestFinding(unittest.TestCase):

    def test_find_none(self):
        self.assertIsNone(plugin.find_jest_configuration_file(None, None))
        self.assertIsNone(plugin.find_jest_configuration_file('', ['']))
        self.assertIsNone(plugin.find_jest_configuration_file(' ', [' ']))
        self.assertIsNone(plugin.find_jest_configuration_file([], []))
        self.assertIsNone(plugin.find_jest_configuration_file('foo', ''))

    def test_find_none_with_file(self):
        file = os.path.join(unittest.fixtures_path(), 'none', 'js', 'index.spec.js')

        self.assertIsNone(plugin.find_jest_configuration_file(file, None))
        self.assertIsNone(plugin.find_jest_configuration_file(file, []))
        self.assertIsNone(plugin.find_jest_configuration_file(file, [' ']))
        self.assertIsNone(plugin.find_jest_configuration_file(file, ['foobarfoobar']))

    def test_find_none_with_folders(self):
        folders = [
            os.path.join(unittest.fixtures_path(), 'none'),
            os.path.join(unittest.fixtures_path(), 'sub', 'site'),
            os.path.join(unittest.fixtures_path(), 'root')
        ]

        self.assertIsNone(plugin.find_jest_configuration_file(None, folders))
        self.assertIsNone(plugin.find_jest_configuration_file('', folders))
        self.assertIsNone(plugin.find_jest_configuration_file(' ', folders))
        self.assertIsNone(plugin.find_jest_configuration_file('foobar', folders))

    def test_find_jest_configuration_file(self):
        # configuration in root dir
        file = os.path.join(unittest.fixtures_path(), 'root', 'js', 'index.spec.js')
        folders = [
            os.path.join(unittest.fixtures_path(), 'root')
        ]
        expected = os.path.join(unittest.fixtures_path(), 'root', 'jest.config.js')
        self.assertEqual(expected, plugin.find_jest_configuration_file(file, folders))

        # configuration in sub dir
        file = os.path.join(unittest.fixtures_path(), 'sub', 'site', 'js', 'index.spec.js')
        folders = [
            os.path.join(unittest.fixtures_path(), 'sub')
        ]
        expected = os.path.join(unittest.fixtures_path(), 'sub', 'site', 'jest.config.js')
        self.assertEqual(expected, plugin.find_jest_configuration_file(file, folders))

        # ts configuration in root dir
        file = os.path.join(unittest.fixtures_path(), 'ts', 'js', 'index.spec.js')
        folders = [
            os.path.join(unittest.fixtures_path(), 'ts')
        ]
        expected = os.path.join(unittest.fixtures_path(), 'ts', 'jest.config.ts')
        self.assertEqual(expected, plugin.find_jest_configuration_file(file, folders))