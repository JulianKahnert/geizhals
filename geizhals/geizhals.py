#!/usr/bin/env python3
import logging
import re
from enum import Enum
from urllib.parse import urlparse

import bs4
import requests

_LOGGER = logging.getLogger(__name__)
_REGEX = r'\D\s(\d*)[\,|\.](\d*)'

class Domain(Enum):
    AT = 'geizhals.at'
    EU = 'geizhals.eu'
    DE = 'geizhals.de'
    UK = 'skinflint.co.uk'
    PL = 'cenowarka.pl'

class Device():
    name = ''
    prices = []
    price_currency = ''

    def __repr__(self):
         return self.__str__()
    def __str__(self):
        return """
Name:       {}
Prices:     {}
Currency:   {}
        """.format(self.name,
                   self.prices,
                   self.price_currency)

class Geizhals():
    locale = ''
    product_id = ''
    _soup = None

    # save parsed data
    device = Device()


    def __init__(self, ID_or_URL, locale = 'DE'):
        """Initialize the sensor."""
        self.locale = Domain[locale].value

        # get the id from a URL
        self.product_id = self._url2id(ID_or_URL)

        # fetch data
        sess = requests.session()
        request = sess.get('https://{}/{}'.format(self.locale,
                                                  self.product_id),
                           allow_redirects=True,
                           timeout=1)
        self._soup = bs4.BeautifulSoup(request.text, 'html.parser')

    def parse(self):
        # parse name
        raw = self._soup.find('h1', attrs={'class': 'gh-headline'})
        self.device.name = raw.string.replace('\n', '')

        # parse prices
        self.device.prices = []
        for tmp in self._soup.select('div.offer__price .gh_price'):
            matches = re.search(_REGEX, tmp.string)
            raw = '{}.{}'.format(matches.group(1),
                                 matches.group(2))
            self.device.prices += [float(raw)]

        # parse unit
        price_match = self._soup.find('span', attrs={'class': 'gh_price'})
        matches = re.search(r'€|£|PLN', price_match.string)
        self.device.price_currency = matches.group()

        return self.device

    def _url2id(self, ID_or_URL):
        try:
            sess = requests.session()
            request = sess.get(ID_or_URL,
                               allow_redirects=True,
                               timeout=1)
        except requests.exceptions.MissingSchema:
            # assuming a valid product_id
            return ID_or_URL

        # get product_id from valid url
        soup = bs4.BeautifulSoup(request.text, 'html.parser')
        phistURL = soup.select('.productpage__overview-links--pricehistory')[0].attrs['href']
        return re.search(r'phist\=(\d+)$', phistURL).group(1)
