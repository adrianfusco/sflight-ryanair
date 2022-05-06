# Sflight

This simple project is used to get information about flights between two airports in a specific date using the RyanAir API.

For now we're searching just for RyanAir flights.

## Usage examples:

```
... (main)$ -> python3 search.py --origin SCQ --destination MAD --departure-date 2022-05-18

Origin: Santiago Comp. 
Destination: Madrid  


2 flights available for day: 2022-05-18T00:00:00.000

  Flight Number: FR 5316
  Duration: 01:10h
  Time UTC:  -> 2022-05-18T06:50:00.000 -> 2022-05-18T08:00:00.000
  Price: 23.89  EUR

  Flight Number: FR 5318
  Duration: 01:10h
  Time UTC:  -> 2022-05-18T22:25:00.000 -> 2022-05-18T23:35:00.000
  Price: 9.99  EUR

____________________________

Origin: Madrid  
Destination: Santiago Comp. 


2 flights available for day: 2022-05-18T00:00:00.000

  Flight Number: FR 5315
  Duration: 01:15h
  Time UTC:  -> 2022-05-18T08:35:00.000 -> 2022-05-18T09:50:00.000
  Price: 31.82  EUR

  Flight Number: FR 5317
  Duration: 01:15h
  Time UTC:  -> 2022-05-18T20:35:00.000 -> 2022-05-18T21:50:00.000
  Price: 40.62  EUR

____________________________
```