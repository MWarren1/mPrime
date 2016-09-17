############
## mPrime ##
############

## v2 - skips even numbers, but misses 2
## v3 - only checks remainder to half of the number

import argparse
import time

## CLI switches
parser = argparse.ArgumentParser(prog='mPrime', description='scans for prime number in range of numbers')
parser.add_argument('--start', help='start of the number range(optional default is 1)')
parser.add_argument('--end', required=True, help='last number in the range')

args = parser.parse_args()
start = args.start
end_num = int(args.end)

if start is None:
	start = 2
start = int(start)
start_time = time.time()	
	
def prime_check(number):
	currentnum = 3
	maxnumber = number
	prime = "YES"
	while currentnum < (maxnumber/2) and prime == "YES":
		remainder = number % currentnum
		#print remainder
		if remainder == 0:
			prime = "NO"
		currentnum = currentnum + 1	
	return prime

num_of_primes = 0	
currentnum = int(start)
if currentnum == 2:
	num_of_primes = 1
	print str(currentnum) + " IS PRIME!"
if currentnum%2 == 0:
	currentnum = currentnum+1
	
while currentnum < end_num:	
	is_prime = prime_check(currentnum)
	if is_prime == "YES":
		print str(currentnum) + " IS PRIME!"
		num_of_primes = num_of_primes +1
	currentnum = currentnum + 2
	
## finish up script
end_time = time.time()
time_taken = (end_time - start_time)
print "#" * 60
print "-" * 60
print "between "+str(start)+" and "+str(end_num)
print "there are "+str(num_of_primes)+" prime numbers"
print "Time Taken : "+str(time_taken)+ " Seconds"
print "-" * 60
print "#" * 60