# Write a program to find the largest among three numbers
x=int(input())
y=int(input())
z=int(input())

if(x>y):
  if(x>z):
    print(x)
  else:
    print(z)
else:
  if(y>z):
    print(y)
  else:
    print(z)