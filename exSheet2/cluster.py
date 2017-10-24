import numpy as np
def main():
	S=np.array([[2,12],[3,11],[3,8],[5,4],[7,5],[7,3],[10,8],[13,8]])
	z=np.array([[2,12],[3,11],[3,8]])
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
	


def newCenter(S,clus):
	sum= np.zeros((3,2))
	for x in range(len(clus)):
		sum[int(clus[x])]+=S[x]
	
	for x in range(0,3):
		sum[x]= sum[x]/np.count_nonzero(clus==x)
	return sum


if __name__ == '__main__':
    main()