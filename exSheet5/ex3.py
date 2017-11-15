import numpy as np
import matplotlib.pyplot as plt


def main():
	points=points_ball()
	for x in points:
		print(np.linalg.norm(x))
	dist=distance(points)
	ang=angle(points)

	plt.figure(1)
	plt.hist(dist,20)
	plt.title("Pairwise distance of points in unit ball")
	
	plt.figure(2)
	plt.hist(ang,20)
	plt.title("Pairwise angle of points in unit ball")

	plt.show()

def points_cube():
	points=[]
	for i in range(30):
		x=np.random.uniform(-0.5,0.5,100)
		points.append(x)
	return points

def points_ball():
	points=[]
	max_norm=0
	for i in range(30):
		x=np.random.uniform(-1,1,100)
		n=np.linalg.norm(x)
		if(n>max_norm):
			max_norm=n
		points.append(x)
	points/=max_norm
	return points

def distance(points):
	dist=[]
	for j in range(len(points)):
		for i in range(len(points)):
			if(j!=i):
				dist.append(np.linalg.norm(points[j]-points[i]))
	return dist

def angle(points):
	ang=[]
	for j in range(len(points)):
		for i in range(len(points)):
			if(j!=i):
				p1=points[j]
				p2=points[i]
				l1=np.linalg.norm(p1)
				l2=np.linalg.norm(p2)
				dprod=np.dot(p1,p2)
				ang.append(np.arccos(dprod/(l1*l2)))

	return ang

if __name__ == '__main__':
    main()
