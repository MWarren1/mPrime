# mPrime
###### Dependencies : Python 2.7
###### By Redemption.Man
Messing around finding efficient script to search for prime numbers, currently 4 different versions. the table below shows how long in seconds each script took to search each number range for all the prime numbers:


|Number Range                 |Version 1 |Verison 2 |version 3 |version 3.5 |Version 4  |
|-----------------------------|----------|----------|----------|------------|-----------|
|1 -10,000                    |1.04      |1.047     |0.73      |0.66        |0.39       |
|1 -25,000                    |5.71      |5.77      |3.91      |3.36        |2.13       |
|1 - 50,000                   |19.53     |19.37     |12.93     |11.67       |7.96       |
|1 - 75,000                   |41.20     |41.21     |28.79     |25.95       |17.33      |
|1 - 100,000                  |72.99     |70.93     |47.04     |42.82       |29.88      |
|1- 250,000                   |393.49    |393.09    |262.27    |240.58      |172.14     |
|100,000,000 -  100,000,100   |90.14     |90.84     |58.06     |53.68       |39.13      |
|1,000,000,000 - 1,000,000,010|299.44    |299.31    |194.58    |175.90      |130.24     |


```
usage: mPrime [-h] [--start START] --end END

scans for prime number in range of numbers

optional arguments:
  -h, --help     show this help message and exit
  --start START  start of the number range(optional default is 1)
  --end END      last number in the range
  ```
