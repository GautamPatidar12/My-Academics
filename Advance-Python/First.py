'''
a="        Aashutosh Kumar Singh"


print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('a','B'))
print(a.replace("Aashutosh","Gudda"))

print(a.split())
print(a.split(" "))
print(a.split("a"))

first="Gautam "
last="Patidar"
print(first+last)

a=5.5
b=7
print(a+b)
a="5.5"
b="7"
print(a+b)

a="   aashutosh kumar singh   "
print(a.title())
print(a.lstrip())
print(a.rstrip())

a=["Aashutosh ","Kumar"]
print("".join(a))

a="Aashutosh Kumar"

print(a.find("z"))
print(a.find("o"))
print(a.find("a"))
print(a.find("K"))


a="123Aashutosh Kumar"
print(a.isalpha())
print(a.isdigit())

a="Gautam Patidar{}"
b=1209
print(a.format(b))

a="{}Gautam Patidar"
b=1209
a.format(b)

a="Gautam Patidar"
print(a.count("a"))
print(ord("a"))
print(ord("A"))
print(ord("@"))
print(ord("."))

p="abcdefghijklmnopqrstuwxyz"
for i in p:
    print(ord(i),end=" ")

for i in p:
    x=i.upper()
    print(ord(x),end=" ")

print(chr(69))'''
a=2004
print(type(a),"\n",str(a),"\n",type(str(a)))

p="abcdefghijklmnopqrstuwxyz"
for i in p:
    print(ord(i),end=" ")