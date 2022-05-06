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

Origin: Santiago Comp.
Destination: Madrid


2 flights available for day: 2022-05-20T00:00:00.000

  Flight Number: FR 5316
  Duration: 01:10h
  Time UTC:  -> 2022-05-20T06:50:00.000 -> 2022-05-20T08:00:00.000
  Price: 28.29  EUR

  Flight Number: FR 5318
  Duration: 01:10h
  Time UTC:  -> 2022-05-20T22:25:00.000 -> 2022-05-20T23:35:00.000
  Price: 51.39  EUR

____________________________

Origin: Madrid
Destination: Santiago Comp.


2 flights available for day: 2022-05-20T00:00:00.000

  Flight Number: FR 5315
  Duration: 01:15h
  Time UTC:  -> 2022-05-20T08:35:00.000 -> 2022-05-20T09:50:00.000
  Price: 9.99  EUR

  Flight Number: FR 5317
  Duration: 01:15h
  Time UTC:  -> 2022-05-20T20:35:00.000 -> 2022-05-20T21:50:00.000
  Price: 89.02  EUR

____________________________
