#Unpacking a Sequence into Separate Variables

#PROBLEM
#You have an N-element tuple or sequence that you would like to unpack into a collection of N variables
p=(4,5)
x,y=p
print (x)
print (y)
#----------------
data = ['acme', 50, 91.1 , (2013,12,21)]
name, age, price, date = data
print (name)
print (age)

#discussion

palabra = "hello"
a,b,c,d,e=palabra
print (a)
print (b)
print (c)
print (d)

#-------
data = ['acme', 50, 90.1, (2012,12,21)]
_, shares,price,_ =data
print (shares)
print(_)