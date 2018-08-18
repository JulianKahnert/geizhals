import unittest
from random import uniform
from time import sleep
from geizhals import geizhals


class TestStringMethods(unittest.TestCase):
    def test_URL_AT(self):
        id = geizhals._url2id("https://geizhals.at/bose-quietcomfort-35-ii-schwarz-a1696985.html")


        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(id, "1696985")

    def test_URL_EU(self):
        id = geizhals._url2id("https://geizhals.eu/bose-quietcomfort-35-ii-schwarz-a1696985.html")

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(id, "1696985")

    def test_URL_DE(self):
        id = geizhals._url2id("https://geizhals.de/bose-quietcomfort-35-ii-schwarz-a1696985.html")

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(id, "1696985")

    def test_URL_UK(self):
        id = geizhals._url2id("https://skinflint.co.uk/bose-quietcomfort-35-ii-black-a1696985.html")

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(id, "1696985")

    def test_URL_PL(self):
        id = geizhals._url2id("https://cenowarka.pl/bose-quietcomfort-35-ii-czarny-a1696985.html")

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(id, "1696985")


if __name__ == '__main__':
    unittest.main()
