#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:14:41 2019

@author: mazeyarmoeini
"""

import math, time
from GraphGeneration import *
import matplotlib.pyplot as plt 

capacity = [[0 for i in range(6)] for j in range(6)]

capacity[0][1] = 16
capacity[0][2] = 13
capacity[1][2] = 10
capacity[1][3] = 12
capacity[2][4] = 14
capacity[2][1] = 4
capacity[3][5] = 20
capacity[3][2] = 9
capacity[4][3] = 7
capacity[4][5] = 4

capacity = GenerateGraph(10)

def residual(C,F):
    return C-F

def relabel_to_front(C, source, sink):
     n = len(C) 
     
     F = [[0 for i in range(n)] * n for x in range(n)]
     
     height = [0 for i in range(n)] 
     extra = [0 for i in range(n)] 
     visited   = [0 for i in range(n)] 

     nodelist = []
     for i in range(n):
         if i != source and i != sink:
             nodelist.append(i)    


     height[source] = n 
     extra[source] = math.inf
     for vertex in range(n):
         supply = min(extra[source], residual(C[source][vertex],F[source][vertex]))
         F[source][vertex] = F[source][vertex] + supply
         F[vertex][source] = F[vertex][source] - supply
         extra[source] = extra[source] - supply
         extra[vertex] = extra[vertex] + supply

     index = 0
     while index < len(nodelist):
         canidate = nodelist[index]
         old_height = height[canidate]
         
         
         while extra[canidate] > 0:
             if visited[canidate] < n: 
                 vertex = visited[canidate]
                 if residual(C[canidate][vertex],F[canidate][vertex]) > 0 and height[canidate] > height[vertex]:
                     supply = min(extra[canidate], 
                                  residual(C[canidate][vertex],
                                  F[canidate][vertex]))
                     F[canidate][vertex] = F[canidate][vertex] + supply
                     F[vertex][canidate] = F[vertex][canidate] - supply
                     extra[canidate] = extra[canidate] - supply
                     extra[vertex] = extra[vertex] + supply
                 else:
                     visited[canidate] += 1
             else: 
                 min_height = math.inf
                 for v in range(n):
                     if residual(C[canidate][v],F[canidate][v]) > 0:
                         min_height = min(min_height, height[v])
                         height[canidate] = min_height + 1
                 visited[canidate] = 0
         
         
         
         if height[canidate] > old_height:
             nodelist.insert(0, nodelist.pop(index)) 
             index = 0 
         else:
             index += 1

     return sum(F[source])
 
print(relabel_to_front(capacity, 0, 5))

def main():

    min_sample = 0
    max_sample = 500
    x, y = [i for i in range(min_sample, max_sample + 1, 10)], []
    
    for node_count in x:
        source_s = 0
        dest_d = node_count 

        Network = GenerateNetwork(node_count)
        Neighbors_Network = GenerateNeighbourMatrix(Network)

        time_taken = time.time()
        
        max_flow = relabel_to_front(capacity, source_s, dest_d)
        
        time_taken = time.time() - time_taken
        
        y.append(time_taken*1000)

    
    fig = plt.figure()
    push_relab_fig = fig.add_subplot(111)
    
    push_relab_fig.set_xlabel('matrix size (nXn)')
    push_relab_fig.set_ylabel('time (milliseconds)')
    
    push_relab_fig.plot(x, y, label='Push-relabel O(V\N{SUPERSCRIPT TWO}E)')
    push_relab_fig.grid(linestyle='-')
    
    legend = push_relab_fig.legend()
    
    plt.show()

if __name__ == '__main__':
    main()