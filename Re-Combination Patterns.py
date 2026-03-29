print("Patern 1")
print()
n=5
for i in range(1,5+1):
    for j in range(1,i-1+1):
        print(" ", end="")
    for j in range(1,n-i+1+1):
        print("*", end="")
    print()
print()

print("Patern 2")
print()
n=4
for i in range(1,n+1):
    for j in range(1,i-1+1):
        print(" ",end="")
    for j in range(1,6+1):
        print("*",end="")
    print()
print()

print("Patern 3")
print()
n=4
for i in range(1,4+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,4+1):
        print("*",end="")
    print()
print()

print("Pattern 4")
print()
n=5
for i in range(1,n):
    print(" "*(n-i-1) + "*"*(i+(i-1)))





