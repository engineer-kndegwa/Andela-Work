class PrimeChecker(object):
  def __init__(self,string=''):
    self.string = string
  def is_prime(self):
	if len(self.string) is 0:
		return False
	else:
		conv = int(self.string)
		if conv > 1:
		  for i in range(2,conv):
		   if (conv % i) == 0:
			 return False
		   elif conv == 2:
			 return True
		   else:
			   return True
         

