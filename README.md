# Sflight

This simple project is used to get information about flights between two airports in a specific date using the RyanAir API.

For now we're searching just for RyanAir flights.

## Installation:

```
$ pip3 install .
Defaulting to user installation because normal site-packages is not writeable
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for sflight-ryanair, since package 'wheel' is not installed.
Installing collected packages: sflight-ryanair
  Running setup.py install for sflight-ryanair ... done
Successfully installed sflight-ryanair-0.0.1
```

```
$ sflight -h
usage: sflight [-h] --departure-date DEPARTURE_DATE --origin ORIGIN --destination DESTINATION

Parse the information required to get information about flights in RyanAir

optional arguments:
  -h, --help            show this help message and exit
  --departure-date DEPARTURE_DATE
  --origin ORIGIN
  --destination DESTINATION
```

## Usage examples:

```
$ sflight --origin SCQ --destination MAD --departure-date 2022-05-20

Origin City     Destination City    Flight number    Flying duration    Time departure -> Time arrival                      Price
--------------  ------------------  ---------------  -----------------  --------------------------------------------------  ---------
Santiago Comp.  Madrid              FR 5316          01:10h             2022-05-20T06:50:00.000 -> 2022-05-20T08:00:00.000  28.29 EUR
Santiago Comp.  Madrid              FR 5318          01:10h             2022-05-20T22:25:00.000 -> 2022-05-20T23:35:00.000  51.39 EUR
Madrid          Santiago Comp.      FR 5315          01:15h             2022-05-20T08:35:00.000 -> 2022-05-20T09:50:00.000  9.99 EUR
Madrid          Santiago Comp.      FR 5317          01:15h             2022-05-20T20:35:00.000 -> 2022-05-20T21:50:00.000  89.02 EUR
```
