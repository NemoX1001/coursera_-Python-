
import math 
 
def isPrime(n): 
  if n <= 1: 
  	return False
  for i in range(2, int(math.sqrt(n)) + 1): 
  	if n % i == 0: 
   	 return False
  return True

n = 2 
count = 0
while (True):
	if (count == 6):
		break
	if isPrime(n):
		m = 2**n - 1
		if isPrime(m):
			print (n,m)
			count = count+1
	n = n+1


	



