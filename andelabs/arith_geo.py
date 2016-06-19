def arith_geo(argument):
  if type(argument) is list:
    if len(argument) == 0:
      return 0
    else:
		div1 = (argument[1]/argument[0])
		div2 = (argument[2]/argument[1])
		div3 = (argument[3]/argument[2])
		num =  (argument[len(argument)-1]) - (argument[0])
		den =  (len(argument) - 1)
		rhs = num/float(den)
		'''Importat because if 7/4 ==1 but 7/float 4 == 1.75'''
		sub1 = (argument[1]-argument[0])
    
		if sub1==rhs :
		  return 'Arithmetic'
		elif (div1==div2) and (div3==div1) :
		  return 'Geometric'
		else:
		  return -1
	
    
