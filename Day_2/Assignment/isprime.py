"""Checking if how many numbers are prime"""
def isPrime(x):
	prime_numbers=[2,3]
	start_point = 4
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
	while True:
		for number in range(2,(start_point//2)+1):
#--------------------------------------------------------------------
#--------------------------------------------------------------------

			if start_point % number == 0:
				break
#--------------------------------------------------------------------

		else:
			prime_numbers.append(start_point)
		start_point+=1
		if len(prime_numbers) == x:
			break
	return prime_numbers
	
print(isPrime(100))
