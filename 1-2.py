#1.2 Unpacking elements from iterables of arbitrary length
#an example would be the humbers of a contact, for example there is a guy who works in a bank, so he have cellphone number, telephone, office phone

record = ('dave', 'dave@example.com','232323', '4464')
#always use * if you  want to do this

name, email, *phone = record
print (name)
print (email)
print (phone)

#-------------------
#an invert way

*group, unit = [10,9,8,7,6,5,4,3,2,1]
print(group)
print(unit)
#discussion

line = 'nobody:*:-2:-2:Unpriviliged User:/var/empty:/usr/bin/false'
uname, *fields,homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)

#simple example

line='a:*:b:2:c'
uno,dos,*tres =line.split(':')
print(uno)
print(dos)
print(tres)

#if you want to ignore some values from the list, you can use '_' or 'ign'
record = ('ACME', 50, 123.45,(12,18,2012))
name,*_,(*_,year)=record
#in this case I use the '_' character
print(name)
print(year)

#an example with a function usign the star unpacking
items = [1,10,7,4,5,9]
def sum(items):
    head,*tail=items
    return head+sum(tail) if tail else head

print(sum(items))