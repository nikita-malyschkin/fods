import numpy as np 

def main(): 
	m1=np.array([[2,-12],[1,-5]])
	m2=np.array([[1,2,0],[-2,1,2],[1,3,1]])
	m3=np.array([[1,1,0],[3,-1,0],[0,0,-2]])
	m4=np.array([[4,5],[6,5]])
	m5=np.array([[-4,10],[7,5]])
	l=iter(m5,400)
	print(l)
	print(rayleigh(m5,l))
	#print(1.0/rayleigh(m1,l))
	

def iter(m,n):
	x=np.ones(len(m))
	#x=np.random.rand(len(m))
	n_iter=0
	for t in range(n):
		xlast=x
		x= np.dot(m,x)
		n_iter+=1
		#print(np.linalg.norm(x))
		x = x/ np.linalg.norm(x,np.inf)
		#x=x/(np.amax(np.abs(x))*np.sign(np.amax(x)))
		if (round(x[0],3)==round(xlast[0],3) and round(x[1],3)==round(xlast[1],3)):
			print(n_iter)
			return x
	return x	

def inv_iter(m,n):
	x=np.ones(len(m))
	#x=np.random.rand(len(m))
	for t in range(n):
		x= np.dot(np.linalg.inv(m),x)
		#print(np.linalg.norm(x))
		x = x/ np.linalg.norm(x,np.inf)
		#x=x/(np.amax(np.abs(x))*np.sign(np.amax(x)))
	return x	

def rayleigh(m,x):
 r1 = np.dot(m,x)
 r2=np.dot(x,r1)

 return r2/np.dot(x,x)

if __name__ == '__main__':
    main()