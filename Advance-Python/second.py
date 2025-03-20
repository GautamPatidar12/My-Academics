'''a="Learning Python"

print(a[6])
print(a[9])
print(a[3])
print(a[-5])

print(a[0:9])
print(a[9:])

for i in a:
    print(i ,end=" ")

print("\n")

for i in range(len(a)):
    print(a[i],end=" ")

print("\n")

for i in range(0,len(a),3):
    print(a[i],end=" ")

for i in range(-1,-len(a)-1,-1):
    print(a[i],end=" ")

print(a[-1::-1])
print(a[::])
print(a[::1])
print(a[::2])
print(a[2:9:2])'''


a=eval(input("Give the string"))

b=a[::]
c=a[-1::-1]
if(b==c):
    print("It is palindrom")
else:
    print("It is no palindrom")