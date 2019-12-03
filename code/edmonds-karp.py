import math
from GraphGeneration import *
import matplotlib.pyplot as plt
import time 

def aug_path_search(Graph_G, Neighb_N, source, dest, Res_R):
    #Graph_G is the adjacency matrix containing the capacity
    #Neighb_N is the adjacency List containing neighbours
    #Res_R is the Residual Flow 
    P = [-1 for x in Graph_G]
    P[source] = -2

    M = [0 for x in Graph_G]
    M[source] = math.inf
    
    Qu = [source]
    Visited = list()
    
    while Qu:
        u = Qu.pop(0)
        Visited.append(u)
        for v in Neighb_N[u]:
            if Graph_G[u][v] > Res_R[u][v]:
                if P[v] == -1:
                    P[v] = u
                    M[v] = min(M[u], Graph_G[u][v] - Res_R[u][v])
                    if v == dest:
                        return M[dest], P, Visited
                    Qu.append(v)
    return 0, P ,Visited

def Edmonds_Karp(Graph_G, Neighb_N, source, dest):

    max_flow = 0
    Res_R = [[0 for i in Graph_G] for i in Graph_G] #residual flow
    
    trace = list()

    while True:
        path_flow, P, visited = aug_path_search(Graph_G, Neighb_N, source, dest, Res_R)

        if path_flow == 0:
            break
            
        trace.append(visited) #able to trace search path

        max_flow += path_flow
        
        vj = dest
        while vj != source:
            vi = P[vj]
            Res_R[vi][vj] = Res_R[vi][vj] + path_flow
            Res_R[vj][vi] = Res_R[vj][vi] - path_flow
            vj = vi

    return max_flow, trace

def main():
    min_sample = 10
    max_sample = 150
    x, y = [i for i in range(min_sample, max_sample + 1)], []
    control_graph = [i**2 for i in range(max_sample - min_sample + 1)]
    for node_count in x:
        source_s = 0
        dest_d = node_count 

        Network = GenerateNetwork(node_count)
        Neighbors_Network = GenerateNeighbourMatrix(Network)
        showGraph(Network)
        print()
        
        time_taken = time.time()
        max_flow, trace  = Edmonds_Karp(Network, Neighbors_Network, source_s, dest_d)
        time_taken = time.time() - time_taken
        y.append(time_taken)

    plt.plot(x, y)
##    plt.plot(control_graph, y)

    plt.show()

if __name__ == '__main__':
    main()
