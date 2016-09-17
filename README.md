# mPrime
###### Dependencies : Python 2.7
###### By Redemption.Man
Messing around finding efficient script to search for prime numbers, currently 4 different versions. the table below shows how long in seconds each script took for the number ranges:


|Number Range           |Version 1   |Verison 2   |version 3   |version 3.5 |Version 4  |
|-----------------------|------------|------------|------------|------------|-----------|
|1 -10,000              |1.046999931 |1.046999931 |0.734999895 |0.657000065 |0.390000105|
|1 -25,000              |5.713000059 |5.76699996  |3.914000034 |3.363000155 |2.131999969|
|1 - 50,000             |19.52900004 |19.36800003 |12.92600012 |11.67199993 |7.955000162|
|1 - 75,000             |41.19499993 |41.20599985 |28.78699994 |25.94700003 |17.32999992|
|1 - 100,000            |72.98899984 |70.92700005 |47.04099989 |42.81500006 |29.88199997|
|1- 250,000             |393.4909999 |393.0869999 |262.2679999 |240.582     |172.1440001|
|100000000 -  100000100 |90.13800001 |90.83500004 |58.05900002 |53.68300009 |39.125     |
|1000000000 - 1000000010|299.441     |299.3109999 |194.579     |175.9000001 |130.24     |


```
usage: mPrime [-h] [--start START] --end END

scans for prime number in range of numbers

optional arguments:
  -h, --help     show this help message and exit
  --start START  start of the number range(optional default is 1)
  --end END      last number in the range
  ```
