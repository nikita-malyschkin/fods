import numpy as np

A=np.array([[1,1,1,1,1,1,1],[0,0,1,0,0,1,0],[0,1,0,1,0,1,1],[0,1,1,0,1,0,0],[0,1,0,0,0,0,0]])
H=np.array([[1,1,1,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,1,1,1,1],[0,1,1,0,1,0,1],[0,1,0,0,1,0,0],])
alpha=1.0/4
e=np.array([0,1,1,0,0,1,1])
w=np.array([1.0,1,1,1,1])
for event in range(len(e)):
	p=np.zeros(5)
	w_sum=0
	for x in range(5):                    #  calculate probabilities for picking experts
		if(H[x][event]==1):
			p[x]=w[x]
			w_sum+=w[x]
	
	
	p/=w_sum

	m=np.zeros(5)                           
	for x in range(5):                    # calculate m
		if A[x,event]!=e[event]:
			m[x]=1
	
	r=np.zeros(5)
	r_sum=0
	for x in range(5):                    # calculate update parameter r
		r[x]=-m[x]
		r_sum+=p[x]*m[x]
	r_sum/= (1+alpha)
	r+=r_sum
	for x in range(5):
		if H[x][event]==1:
			w[x]*=(1+alpha)**r[x]		  # update active experts

	print(w)
