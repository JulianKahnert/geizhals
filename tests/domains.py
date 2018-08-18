import unittest
from random import uniform
from time import sleep
from geizhals import Geizhals


class TestStringMethods(unittest.TestCase):
    # test with ID
    def test_ID_AT(self):
        gh = Geizhals(1688629, "AT")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_ID_EU(self):
        gh = Geizhals(1688629, "EU")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_ID_DE(self):
        gh = Geizhals(1688629, "DE")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_ID_UK(self):
        gh = Geizhals(1688629, "UK")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grey")

    def test_ID_PL(self):
        gh = Geizhals(1688629, "PL")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB szary")

    # test with URL
    def test_URL_AT(self):
        gh = Geizhals("https://geizhals.at/apple-iphone-x-64gb-grau-a1688629.html", "AT")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_URL_EU(self):
        gh = Geizhals("https://geizhals.eu/apple-iphone-x-64gb-grau-a1688629.html", "EU")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_URL_DE(self):
        gh = Geizhals("https://geizhals.de/apple-iphone-x-64gb-grau-a1688629.html", "DE")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grau")

    def test_URL_UK(self):
        gh = Geizhals("https://cenowarka.pl/apple-iphone-x-64gb-szary-a1688629.html", "UK")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB grey")

    def test_URL_PL(self):
        gh = Geizhals("https://cenowarka.pl/apple-iphone-x-64gb-szary-a1688629.html", "PL")
        device = gh.parse()

        # avoid banning from website
        sleep(uniform(1, 10))

        self.assertEqual(device.name, "Apple iPhone X 64GB szary")


if __name__ == '__main__':
    unittest.main()
