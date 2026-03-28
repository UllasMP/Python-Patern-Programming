print("Pattern 1")
print()
n=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i+j==n+1:
            print("*", end="")
        else:
            print(" ",end="")
            
    print()
print()

print("pattern 2")
print()
n=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i==j:
            print("*", end="")
        else:
            print(" ",end="")
            
    print()
    
print()

print("Pattern 3")

print()
n=5
for i in range(1,5+1):
    for j in range(1, 5+1):
        if i==j or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

print("Patern 4")
print()
n=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i+j==n+1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

print("Pattern 5")
print()

n=5
for i in range(1,5+1):
    for j in range(1, 5+1):
        if i==j or j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,5+1):
        if i+j==n+1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    
    print()
print()

print("Pattern 6")
print()
n=10
for i in range(1,10):
    for j in range(1,10):
        if i+j==6 or i==j-4 or i==j+4 or i+j==n+4:
            print("*",end="")
        else:
            print(" ",end="")
    print()


print()
print("Pattern 7")
print()
n=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i==1 or j==1 or i==n or j==n:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print()

print("Pattern 8")
print()
n=5
for i in range(1,5+1):
    for j in range(1,5+1):
        if i==1 or j==1 or i==n or j==n or j==3 or i==3:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
print()

print("Pattern 9")
print()

n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 or j==5 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
