import numpy as np
import itertools as iter

x=np.array([[4,2,1],[-1,2,-4],[8,-2,-3],[1,-1,1],[2,-2,5],[-6,2,7]])
y=np.array([-1,1,1,-1,-1,-1])
a=np.arange(0,6)
i=iter.permutations(a)


for perm in i:
	finished=False
	w=np.array([0,0,0])
	steps=0
	while (finished==False):
	    finished=True
	    for t in range(0,6):    
	        if (np.sign(np.dot(w,x[perm[t]]))!=y[perm[t]]):
	            w=w+y[perm[t]]*x[perm[t]]
	            steps+=1
	            print(w)    
	            finished=False
	print("Finished in "+str(steps)+" steps")
	print(perm)
	print("\n")

    
  