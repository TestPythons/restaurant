import sys
import os
import collections

orderedDict=collections.OrderedDict()
from collections import OrderedDict


dish1 = "dish1"
dish2= "dish2"
dish3= "dish3"
rest1= "rest1"
rest2= "rest2"
rest3 = "rest3"
rest4 = "rest4"
dictionary = { "dish1" : { "rest1" : 100,
                         "rest3" : 50,},
               "dish2" : {"rest2"  : 50 ,
                        "rest3"  : 75,
                        "rest4"  : 200},
               "dish3" :  {"rest3" :300,
                         "rest1" :200}

               }

def suggestion(dic):
    #print(orderedDict(sorted(dic.items(), key=lambda t:t[1])).keys())
    s = (sorted(dic.items(), key=lambda t:t[1]))
    print (s)
    for x in s:
        print (x[0])
    #print(dic1.keys())
    #print(dic1.keys())


menu_order=input("input yor favourite dish")
"""if (menu_order=="dish1"):
    dic=dictionary["dish1"]
    #print("\n".join(dic.keys()))
    suggestion(dic)
   
elif(menu_order==dish2):
    dic=dictionary["dish2"]
    #print("\n".join(dic.keys()))
    suggestion(dic)
else :
    dic=dictionary["dish3"]
    #print("\n".join(dic.keys()))
    suggestion(dic)"""

if (menu_order in dictionary.keys()):
    dic=dictionary[menu_order]
    suggestion(dic)
    
    
            
