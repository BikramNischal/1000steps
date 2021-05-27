# simulation for a random walk
# every step taken is calculated as 1 increment/decrement in previous coordinate
# example (x,y) = (1,1) be the last/revious coordinate
# then the next step can any of the given coordinates
# (2,1) or (1,2) or (0,1) or (1,0)

from random import choice
import matplotlib.pyplot as plt
from math import sqrt

# initial position of the persion
init_x , init_y = 0,0


def random_walk():  
	# chooses a coordiante from [(1,0),(0,1),(-1,0),(0,-1)] randomly 
    (dx,dy) = choice(((1,0),(0,1),(-1,0),(0,-1)))
    return dx,dy

def displacement(init_x, init_y, final_x, final_y) -> float:
	return sqrt((final_x-init_x)**2 +(final_y-init_x)**2)


def plotCods():
	fig = plt.figure()
	fig.suptitle("Random Walk", fontsize=15, fontweight ="bold")
	ax = fig.add_subplot()
	
	# this plots the initial position/coordinate of the persion as "o" in the graph
	#ax.plot(init_x,init_y, marker = "o", markersize= 8, markerfacecolor = "red" )
	ax.plot(0,0,marker=".",markersize = 10,markerfacecolor="red")
	ax.text(0,0,"Initial Position")
	px,py = init_x, init_y
	md = 0
	sd = 0
	x = [0]
	y = [0]

	# calculate 1000 random steps and plot each of the coordinate in graph
	for i in range(1000):
	    dx,dy = random_walk()
	    px += dx
	    py += dy
	    x.append(px)
	    y.append(py)
	    d = displacement(init_x, init_y, px,py)
	    if d > md:
	    	md = d
	    sd += d


	    ax.plot(x,y,color = "blue", linestyle = "dotted", linewidth = 1, marker = ".", markersize = 2)
	  	
	# title for graph (maxdisplacement and avarage displacement included)
	ax.plot(px,py,marker=".", markersize=10,markerfacecolor = "red")
	ax.text(px,py,"Final Position")	   
	dis1 = str("Max Displacement = %.4f  " %md)
	dis2 = str("Average Displacement = %.4f" %(sd/1000))
	title = dis1 + dis2
	ax.set_title(title)


	plt.show()



plotCods()
