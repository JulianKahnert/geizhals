#!/usr/bin/env python3
"""Parse prices of a device from the Geizhals website."""
import logging
import re
from enum import Enum

from bs4 import BeautifulSoup
import requests

_LOGGER = logging.getLogger(__name__)
_REGEX = r'\D\s(\d*)[\,|\.](\d*)'


class Domain(Enum):
    """Possible localisations."""

    AT = 'geizhals.at'
    EU = 'geizhals.eu'
    DE = 'geizhals.de'
    UK = 'skinflint.co.uk'
    PL = 'cenowarka.pl'


class Device():
    """Device data which gets parsed by Geizhals."""

    def __init__(self):
        """Initialize device data."""
        self.name = ''
        self.prices = []
        self.price_currency = ''

    def __repr__(self):
        """Call pretty print to get all informaiton."""
        return self.__str__()

    def __str__(self):
        """Pretty-Print all the device data."""
        return """
Name:       {}
Prices:     {}
Currency:   {}
        """.format(self.name,
                   self.prices,
                   self.price_currency)


class Geizhals():
    """Implementation of Geizhals."""

    def __init__(self, id_or_url, locale='DE'):
        """Initialize the sensor."""
        self.locale = Domain[locale].value

        # get the id from a URL
        self.product_id = _url2id(id_or_url)

        # save parsed data
        self.device = Device()

    def parse(self):
        """Get new data, parses it and returns a device."""
        # fetch data
        sess = requests.session()
        request = sess.get('https://{}/{}'.format(self.locale,
                                                  self.product_id),
                           allow_redirects=True,
                           timeout=2)
        sess.close()

        # raise exception, e.g. if we are blocked because of too many requests
        request.raise_for_status()

        soup = BeautifulSoup(request.text, 'html.parser')

        # parse name
        raw = soup.find('h1', attrs={'class': 'gh-headline'})
        self.device.name = raw.string.replace('\n', '')

        # parse prices
        self.device.prices = []
        for tmp in soup.select('div.offer__price .gh_price'):
            matches = re.search(_REGEX, tmp.string)
            raw = '{}.{}'.format(matches.group(1),
                                 matches.group(2))
            self.device.prices += [float(raw)]

        # parse unit
        price_match = soup.find('span', attrs={'class': 'gh_price'})
        matches = re.search(r'€|£|PLN', price_match.string)
        self.device.price_currency = matches.group()

        return self.device


def _url2id(id_or_url):
    try:
        sess = requests.session()
        request = sess.get(id_or_url,
                           allow_redirects=True,
                           timeout=2)
        sess.close()

        # raise exception, e.g. if we are blocked because of too many requests
        request.raise_for_status()

    except requests.exceptions.MissingSchema:
        # assuming a valid product_id
        return id_or_url

    # get product_id from valid url
    soup = BeautifulSoup(request.text, 'html.parser')
    phist_url = soup.select(
        '.productpage__overview-links--pricehistory')[0].attrs['href']
    return re.search(r'phist\=(\d+)$', phist_url).group(1)
