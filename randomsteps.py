# simulation for a random walk
# every step taken is calculated as 1 increment/decrement in previous coordinate
# example (x,y) = (1,1) be the last/revious coordinate
# then the next step can any of the given coordinates
# (2,1) or (1,2) or (0,1) or (1,0)

from random import choice
import matplotlib.pyplot as plt
from math import sqrt

final_x = []
final_y = []


def random_walk():  
	# chooses a coordiante from [(1,0),(0,1),(-1,0),(0,-1)] randomly 
    (dx,dy) = choice(((1,0),(0,1),(-1,0),(0,-1)))
    return dx,dy

def displacement(init_x, init_y, final_x, final_y) -> float:
	return sqrt((final_x-init_x)**2 +(final_y-init_x)**2)

def calcDisplacement():
	global final_x,final_y
	maxd = 0
	sumd = 0

	for i in range(len(final_x)):
		d = displacement(0,0, final_x[i], final_y[i])
		sumd+=d
		if maxd < d:
			maxd = d
	return maxd,sumd/len(final_x)

def getcoordiantes():
	x = [0]
	y = [0]
	px,py = x[0], y[0]

	# calculate 1000 random steps and plot each of the coordinate in graph
	for i in range(1000):
	    dx,dy = random_walk()
	    px += dx
	    py += dy
	    x.append(px)
	    y.append(py)

	return x,y


def plotCods():
	fig = plt.figure()
	fig.suptitle("Random Walk", fontsize=15, fontweight ="bold")
	ax = fig.add_subplot()
	colors = ["red", "blue", "cyan", "green", "yellow", "black","magenta"]
	global final_x,final_y

	# plot graph for 1000 different people 
	for i in range(1000):
		c = choice(colors)
		x,y = getcoordiantes()
		final_x.append(x[-1])
		final_y.append(y[-1])
		ax.plot(x,y,color = c, linestyle = "dotted", linewidth = 1, marker = ".", markersize = 2)
	
	# claculate max and average displacement
	dm, da = calcDisplacement()
	dist = "Max Displacement = %.3f Average Displacement = %.3f" %(dm,da)
	ax.set_title(dist) #set the max and average displacement as subplot titleb

	plt.show()



plotCods()
