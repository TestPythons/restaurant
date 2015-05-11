import sys
import sqlite3
import os

dish=["Dosa"]
Rest_name=["Adigas", "MTR", "Shanti Sagar", "A2B"]
price=[40,60,50, 70]
Rank=[2,1,2,3]

#menu = input("enter the dish")
grade = int(input("enter the rank"))
connection = sqlite3.Connection("Restaurantdb.db")
connection.execute("drop table Restaurant1")
connection.execute("create table Restaurant1(Rest_name varchar(20), dish_name varchar(20), price INTEGER, Rank INTEGER)")
connection.execute("INSERT into Restaurant1 values(?,?,?,?)",(Rest_name[0], dish[0], price[0],Rank[0]))
print("first restaurant added")
connection.execute("INSERT into Restaurant1 values(?,?,?,?)",(Rest_name[1], dish[0],price[1],Rank[1]))
print("second restaurant added")

connection.execute("INSERT into Restaurant1 values(?,?,?,?)",(Rest_name[2], dish[0],price[2],Rank[2]))

connection.execute("INSERT into Restaurant1 values(?,?,?,?)",(Rest_name[3], dish[0],price[3],Rank[3]))

connection.commit()
conn = sqlite3.Connection("Restaurantdb.db")
#print ("The grage is ", grade)
l=conn.execute("select Rest_name from Restaurant1 where Rank = ?",(grade,))
c=l.fetchall()
print(c)
#print(c.rowcount())
connection.close()
