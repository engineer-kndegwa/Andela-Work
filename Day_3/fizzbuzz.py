def fizz_buzz(n):
	"""
	Return fizz when n is dvivisbile by 3
	buzz when divisible by 5
	return fizzbuzz when divisible by 15
	"""
	if n % 3 == 0 and n % 5 == 0:
		return 'fizzbuzz'
	elif n % 3 == 0:
		return 'fizz'
	elif n % 5 == 0:
		return 'buzz' 
	
		
