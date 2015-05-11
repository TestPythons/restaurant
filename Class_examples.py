import random
import os
import sys

class Animal:
    __height =0
    __name = 0
    __weight =0

    def __init__(self, name, height, weight):
        self.__name=name
        self.__height=height
        self.__weight=weight

    def toString(self):
        return "{} is {} cm tall and {} kg".format(
            self.__name,self.__height,self.__weight)



cat = Animal('panther', 50, 20)
print(cat.toString())


class Dog(Animal):
    __owner=" "
    
    def __init__(self,name,height,weight,owner):  
        self.__owner=owner
        super(Dog, self).__init__(name, height, weight)

    def toString(self):
         return "{} is {} cm tall and {} kg and {} is owner".format(
            self.__name,self.__height,self.__weight,self.__owner)


dog=Dog("dalmison",30, 10,"manju")
print(dog.toString())
            
     
