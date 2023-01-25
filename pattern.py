#simple solid squre star print 
n=4
# outer for loop
for i in range(n):
    # inner for loop
    for j in range(n):
        print("*",end=" ")
    print()

# simple solid squre of dolor
m=int(input())
for i in range(m):
    for j in range(m):
        print("$",end=" ")
    print()

# increasing triangle or half pyramid
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# Decreasing triangle or revers pattern
n=6
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

# hill patern
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

        