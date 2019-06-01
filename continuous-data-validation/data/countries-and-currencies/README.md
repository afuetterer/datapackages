A Foreign Key example linking two CSV files in the same data package
---

There are two csv files described in the ressources section of the data package:

- currencies.csv
- countries-using-usd-and-gbp.csv


## Currencies

In currencies.csv are three columns:
- currency_alphabetic_code
- currency
- symbol

An example row is:

currency_alphabetic_code|currency|symbol
--- | --- | ---
USD|US Dollar|$


The primary key is *currency_alphabetic_code* => "USD"


## Countries using USD and GBP currencies

In "countries-using-usd-and-gbp.csv" are two columns:
- name
- currency_alphabetic_code

An example row is:

name|currency_alphabetic_code
--- | ---
American Samoa|USD

The primary key is *name* => "American Samoa"

## Foreign key relationship

A foreign key is defined in the resource countries-using-usd-and-gbp.csv.

The field *currency_alphabetic_code* is defined as a foreign key that points to 
the field *currency_alphabetic_code* in the resource *currencies*.