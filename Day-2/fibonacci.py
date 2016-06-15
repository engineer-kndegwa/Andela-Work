def fibon(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0 
   #Using recursion           
   else:                      
      return fibon(n-1) + fibon(n-2)

#Validation test for first 5 NUmbers in the series
#------------------------------------------------
for i in range(0, 5):
    print(fibon(i))
