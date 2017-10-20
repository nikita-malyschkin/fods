import numpy as np
import matplotlib.pyplot as plt
class Point:
	def __init__(self,a,b):
		self.x = a
		self.y = b

a=Point(2,12)
b=Point(3,11)
c=Point(3,8)
d=Point(5,4)
e=Point(7,5)
f=Point(7,3)
g=Point(10,8)
h=Point(13,8)

l=[a,b,c,d,e,f,g,h]
z=[a,b,c]
z[0].x+=1
print(z[0].x)
print(a[0].x)
change=True
while change :
	change=False

#x=[]
#y=[]
#for p in l:
#	x.append(p.x)
#	y.append(p.y)
#plt.scatter(x,y)
#plt.show()
