import sys
import os
import random

t=int(input("enter number of test cases"))



def markmultiples(plist, a , n):
    i=2
    while((i*a)<=n):
        num=i*a
        plist[num-1]=1
        i+=1

def sieve(m,n):
    if(n>=2):
         plist=[0]*(n)
         for i in range (1,n):
             if(plist[i]==0):
                 if (i+1 >=m):
                    print(i+1)
                 markmultiples(plist, i+1,n)
             
'''n=int(input("enter the number"))
sieve(n)'''    


for x in range (t):
    m=int(input("enter num1"))
    n=int(input("enter num2"))
    if( n -m <= 100000):
        sieve(m,n)
    



















    
