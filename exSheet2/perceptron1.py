import numpy as np
w=np.array([0,0,0])
x=np.array([[4,2,1],[-1,2,-4],[8,-2,-3],[1,-1,1],[2,-2,5],[-6,2,7]])
y=np.array([-1,1,1,-1,-1,-1])
finished=False

steps=0
while (finished==False):
    finished=True
    for t in range(0,6):    
        if (np.sign(np.dot(w,x[t]))!=y[t]):
            w=w+y[t]*x[t]
            steps+=1
            print(w)    
            finished=False
print("Finished in "+str(steps)+" steps")

    
            

