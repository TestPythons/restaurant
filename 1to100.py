import sys
import random
import math
prime_list=[]
n = int(input("enter positive number"))
def check_prime(x):
    for num in range(2,int(math.sqrt(x)+1)):
        if(x % num == 0):
            return False
    return True   
if (n >1):
    for x in range(2,n+1):
       if (check_prime(x)):
            prime_list.append(x)
    print(prime_list)
else :
    print ("enter number greater than 1")

       


        
    
    
    
