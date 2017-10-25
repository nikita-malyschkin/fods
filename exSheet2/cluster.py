import numpy as np
import matplotlib.pyplot as plt
def main():
	S=np.array([[2,12],[3,11],[3,8],[5,4],[7,5],[7,3],[10,8],[13,8]])
	z=np.array([[6, 10], [3, 8], [6, 4], [16.5, 6]])
	clus=np.zeros(8)

	changed=True
	while(changed==True):
		lclus=clus	
		clus=np.zeros(8)
		for x in range(0,8):
			dist=[0,0,0]
			for t in range(0,3):
				dist[t]=np.linalg.norm(S[x]-z[t])
			clus[x]=np.argmin(dist)
		print(clus)
		print(lclus)
		if(all(clus==lclus)):
			changed=False
		z=newCenter(S,clus)
		print(z)


	x=[]
	y=[]
	xz=[]
	yz=[]
	for a in range(len(S)):
		x.append(S[a][0])
		y.append(S[a][1])
	for a in range(len(z)):
			xz.append(z[a][0])
			yz.append(z[a][1])
	plt.scatter(x,y)
	plt.scatter(xz,yz)
	t1=np.arange(-5.0,15.0,0.1)
	plt.plot(t1,f12(t1))
	plt.plot(t1,f13(t1))
	plt.plot(t1,f23(t1))
	axes = plt.gca()
	axes.set_xlim([0,15])
	axes.set_ylim([0,15])
	n=['A','B','C,P2','D','E','F','G','H']
	for i, txt in enumerate(n):

   		axes.annotate(txt, (x[i],y[i]))
   	n2=['P1','','P3']
   	for i, txt in enumerate(n2):

   		axes.annotate(txt, (xz[i],yz[i]))

	plt.show()


def newCenter(S,clus):
	sum= np.zeros((3,2))
	for x in range(len(clus)):
		sum[int(clus[x])]+=S[x]
	
	for x in range(0,3):
		sum[x]= sum[x]/np.count_nonzero(clus==x)
	return sum

def f12(x):
	return 1.0/32.0 * (4*x+309)
def f13(x):
	return (1180.0*x+4833)/1280
def f23(x):
	return 1.0/40.0*(90*x-241)


if __name__ == '__main__':
    main()

