# geizhals

The geizhals library will give you the best price of a product from Geizhals or a related site.
This information can be used in automations, e.g. to notify you when a price drops.


## Install

```bash
pip install geizhals
```

## Usage

```python
from geizhals import Geizhals

# setup the product data
ID_or_URL = 'https://geizhals.de/bose-quietcomfort-35-ii-schwarz-a1696985.html'

# the id of the product is also valid
#ID_or_URL = 1696985

# possible values: AT/EU/DE/UK/PL
locale = 'DE'

# parse the data
obj = Geizhals(ID_or_URL, locale)
device = obj.parse()

# print the available product information
print(device)
```

Get the `product_id` from the geizhals website of your chosen product by opening the *Price History* in a new browser tab (right-click on the price history > open in new tab).
The URL of this site reveals the ID, e.g. `https://geizhals.de/?phist=1696985` with a `product_id` of `1696985`.
