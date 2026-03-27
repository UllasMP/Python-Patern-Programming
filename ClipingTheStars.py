print("Pattern 1")
for i in range(1,5+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print()

print("Pattern 2")
for i in range(1,5+1):
    for j in range(1,i+i-1+1):
        print("*",end="")
    print()
print()

print("Pattern 3")
n=5
for i in range(1,5+1):
    for i in range(1,n-i+1+1):
        print("*",end="")
    print()
print()


print("Pattern 4")
n=5
for i in range(1,5+1):
    for i in range(1,n-i+n-i+1+1):
        print("*",end="")
    print()
print()

print("Same patern Diffrent Method")
print()

print("Pattern 5")
for i in range(1,5+1):
    print("*"*i, end="")
    print()
print()

print("Pattern 6")
for i in range(1,5+1):
    print("*"*(i+i-1),end="")
    print()
print()

print("Pattern 7")
n=5
for i in range(1,5+1):
    print("*"*(n-i+1), end="")
    print()
print()

print("Pattern 8")
n=10
for i in range(1,10+1,2):
    print("*"*(n-i), end="")
    print()
print()


