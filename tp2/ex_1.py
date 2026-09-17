import copy

a=['A']
c=copy.copy(a)
b=a
b[0]=1
print(a,b,c)