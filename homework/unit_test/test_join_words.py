import unittest
from datetime import datetime
from unittest.mock import patch

import requests

from join_words import join_words


def mocked_get(*args, **kwargs):
    return "badger-racoon"


def mocked_get_google(*args, **kwargs):
    return "<Response [404]>"


class TestJoinWords(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("A test suite begins")

    @classmethod
    def tearDownClass(cls):
        print("A test suite ends")

    def setUp(self):
        print("A test begins")

    def tearDown(self):
        print("A test ends")

    def test_join_simple_words(self):
        print("Running... test_join_simple_words")
        result = join_words("holly", "molly")
        self.assertEqual(result, "holly-molly")

    def test_join_complex_words(self):
        print("Running... test_join_complex_words")
        result = join_words("one-two", "three-four")
        self.assertEqual(result, "one-two-three-four")

    @unittest.skip("Second word is still discussed")
    def test_skip_test(self):
        print("Running... test_skip_test")
        result = join_words("great", "")
        self.assertEqual(result, "great-")

    @unittest.expectedFailure
    def test_join_word_and_number(self):
        print("Running... test_join_word_and_number")
        result = join_words("top", 1)
        self.assertEqual(result, "top-one")

    @patch("requests.get", side_effect=mocked_get)
    def test_mock(self, mock):
        print("Running... test_mock")
        response = requests.get("https://www.google.com/search?q=badger")
        self.assertEqual(response, "badger-racoon")

    @unittest.skipIf(datetime.now().weekday() in [0, 2, 4],
                     "Skipped because today is Monday, Wednesday or Friday")
    def test_skip_if_test(self):
        print("Running... test_skip_if_test")
        result = join_words("tic", "tac")
        self.assertEqual(result, "tic-tac")

    @patch("requests.get", side_effect=mocked_get_google)
    def test_google(self, mock):
        print("Running... test_google")
        response = requests.get("https://www.google.com")
        self.assertEqual(response, "<Response [404]>")

