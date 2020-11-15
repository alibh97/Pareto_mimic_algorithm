# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
from numpy.linalg import norm
import numpy as np
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_file(name):
    f=open(name,'r') # open file
    n=int(f.readline().removeprefix('n '))  # read n = number of vertices
    p=int(f.readline().removeprefix('m '))  # read p = number of paths
    tmax=float(f.readline().removeprefix('tmax '))  # read Tmax = available time budget per path

    nodes = []  # a list to append the nodes(points) in it
    for line in f:
        x, y, s = line.split('\t')  # extract x coordinate , y coordinate and score from rest of the lines
        nodes.append([float(x),float(y),int(s)])  # append nodes to nodes list
    return n,p,tmax,nodes  # return extracted variables

def initialization():
    current_node=[] # current node
    mu=0 # number of unvisited feasible nodes
    y=10 # an integer parameter
    l=min(mu,y)

    cost=0 # the travel time of an edge
    reward=0 # the reward of a node

    # if (l!=0) :
    #
    # else:
    #
    #     # bla bla
    x=[]
    return x


# for any node i (1<= i <=n ) ,the nodes except 0, i,and n + 1 ,
# are sorted in descending order according to their static preference values,
# and then the first L nodes are stored into a list of node i,
# where L a sufficient large integer (in our experiment, L is chosen as 50).
def favorite_nodes(nodes):
    static_preference_values=[]

    # for i in range(1,len(nodes)-1):
    #

# suppose current node is i ,static preference value of node j , is r_j / c_ij ,
# r_j is the reward of node j , and c_ij is the travel time of edge(i,j)
def static_preference_values(nodes,index):

    for j in range(1,len(nodes)):
        a=np.array([nodes[index][0],nodes[index][1]])
        b=np.array([nodes[j][0],nodes[j][1]])
        c_ij=norm(a-b)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N,P,Tmax,Points=read_file('p1.2.a.txt')  # extract variables from the file ,
    # N is the number of vertices
    # P is the number of paths
    # Tmax is the available time budget per path
    # points is a list of nodes(points) with their x & y coordinates and scores

    # print('n= ', N,'\np= ',P,'\nTmax= ',Tmax,'\nPoints= ',Points)
    print(norm(np.array([Points[0][0],Points[0][1]])-np.array([Points[1][0],Points[1][1]])))

    # line 1 in algorithm 1
    IS =[]  # incumbent solution needs to be empty at first, it's a set of solution(x)s

    # line 2 in algorithm 1
    Xb=[]  # the best so far solution

    # line 3 in algorithm 1
    # for i in range(N) :
    #     # line 4 in algorithm 1
    #     x = initialization()
    #
    #     # line 5 in algorithm 1
    #     IS.append(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
