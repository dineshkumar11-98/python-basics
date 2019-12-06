a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(b+c>a and a+c>b and a+b>c):
  print("yes")
else:
  print("no")
