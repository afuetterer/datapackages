from datapackage import Package, helpers, exceptions
from copy import deepcopy
from pprint import pprint

import pytest
import json

with open('datapackage.json') as f:
    FK_DESCRIPTOR = json.load(f)


resource = Package(FK_DESCRIPTOR).get_resource('countries-using-usd-and-gbp')
print(resource)
rows = resource.read(relations=True)
for row in rows:
    print(row)
