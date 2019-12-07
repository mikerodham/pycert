# pycert

Read certificates of domains in python.

## How to use

`./pycert.py [hostname]`

Ensure `pycert.py` is an executeable, which we can do with:

`chmod +x pycert.py`

Example:

`./pycert.py github.com`

Output:

```
/**************************************/
/*    github.com/mikerodham/pycert    */
/**************************************/

SUBJECT: github.com
Issued to: github.com
Valid From: May  8 00:00:00 2018 GMT
Valid Until: Jun  3 12:00:00 2020 GMT

ISSUER: DigiCert SHA2 Extended Validation Server CA
```

## Todo

Filter through this mess to make more readable.
You can receive the below by just printing the `cert` var.

```
{
    'crlDistributionPoints': (u 'http://crl3.digicert.com/sha2-ev-server-g2.crl', u 'http://crl4.digicert.com/sha2-ev-server-g2.crl'),
    'subjectAltName': (('DNS', 'github.com'), ('DNS', 'www.github.com')),
    'notBefore': u 'May  8 00:00:00 2018 GMT',
    'caIssuers': (u 'http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt', ),
    'OCSP': (u 'http://ocsp.digicert.com', ),
    'serialNumber': u '0A0630427F5BBCED6957396593B6451F',
    'notAfter': 'Jun  3 12:00:00 2020 GMT',
    'version': 3L,
    'subject': ((('businessCategory', u 'Private Organization'), ), (('jurisdictionCountryName', u 'US'), ), (('jurisdictionStateOrProvinceName', u 'Delaware'), ), (('serialNumber', u '5157550'), ), (('countryName', u 'US'), ), (('stateOrProvinceName', u 'California'), ), (('localityName', u 'San Francisco'), ), (('organizationName', u 'GitHub, Inc.'), ), (('commonName', u 'github.com'), )),
    'issuer': ((('countryName', u 'US'), ), (('organizationName', u 'DigiCert Inc'), ), (('organizationalUnitName', u 'www.digicert.com'), ), (('commonName', u 'DigiCert SHA2 Extended Validation Server CA'), ))
}
```

## MIT License
[The MIT License](http://opensource.org/licenses/MIT)
