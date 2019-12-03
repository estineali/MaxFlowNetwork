import matplotlib.pyplot as plt 
from GraphGeneration import *
import random
import time, math

#######EDMONDS KARP
def aug_path_search(Graph_G, source, dest, Res_R):
    #Graph_G is the adjacency matrix containing the capacity
    #Res_R is the Residual Flow 
    P = [-1 for x in Graph_G]
    P[source] = -2

    M = [0 for x in Graph_G]
    M[source] = math.inf
    
    Qu = [source]
    
    Neighb_N = GenerateNeighbourMatrix(Graph_G)

    while Qu:
        u = Qu.pop(0)
        for v in Neighb_N[u]:
            if Graph_G[u][v] > Res_R[u][v]:
                if P[v] == -1:
                    P[v] = u
                    M[v] = min(M[u], Graph_G[u][v] - Res_R[u][v])

                    if v == dest:
                        return M[dest], P
                    Qu.append(v)
    return 0, P

def Edmonds_Karp(Graph_G, source, dest):

    if dest == len(Graph_G):
        dest -= 1
        
    max_flow = 0
    Res_R = [[0 for i in Graph_G] for i in Graph_G] #residual flow

    while True:
        path_flow, P = aug_path_search(Graph_G, source, dest, Res_R)

        if not path_flow:
            break
            
        max_flow += path_flow
        
        vj = dest
        while vj != source:
            vi = P[vj]
            Res_R[vi][vj] = Res_R[vi][vj] + path_flow
            Res_R[vj][vi] = Res_R[vj][vi] - path_flow
            vj = vi

    return max_flow


#######PUSH RELABEL
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
 
#######DINIC'S
class Graph:
    __V = None
    __levels = None
    __visited = None
    __G = None

    def __init__(self, V):
        self.__V = V
        self.__levels = []
        self.__visited =[]

        for v in range(self.__V):
                self.__levels.append(-1)

        for v in range(self.__V):
                self.__visited.append(0)

        # self.__G = [[0, 10, 10 ,0,0, 0],
        #                       [0, 0,2,4,8, 0],
        #                       [0, 0,0,0,9, 0],
        #                       [0, 0,0,0,0, 10],
        #                       [0, 0,0,6,0, 10],
        #                       [0, 0,0,0,0, 0]]

        self.__G = GenerateNetwork(V)


    def get_graph(self, copy=False):
        #Winchester
        return self.__G

    def showGraph(self):
        for v in range(self.__V):
            print(v, ":", self.__G[v])

    def BFS(self, s):
        for v in range(self.__V):
            self.__levels[v] = -1
        self.__levels[s] = 0

        q = []
        q.append(s)

        while len(q) != 0:
            u = q.pop()

            for v in range(self.__V) :
                if (self.__levels[v] < 0) and (self.__G[u][v] > 0): 
                    self.__levels[v] = self.__levels[u] + 1
                    q.append(v)

    def DFS(self, u,  t, flow):

        if u == t:
            return flow

        while self.__visited[u] < self.__V:
            v = self.__visited[u]
            self.__visited[u] = v + 1

            if (self.__levels[u] < self.__levels[v] ) and (self.__G[u][v] > 0) :
                currFlow = min(flow, self.__G[u][v])
                tempFlow = self.DFS(v, t, currFlow)

                if tempFlow > 0:
                    self.__G[u][v] = self.__G[u][v] - tempFlow
                    self.__G[v][u] = self.__G[v][u] + tempFlow
                    return tempFlow

        return 0 

    def DinicMaxFlow(self, s, t):
        total  = 0

        while True:
            self.BFS(s)
            if self.__levels[t] < 0:
                return total
            # print("Levels:", self.__levels)

            for v in range(self.__V):
                self.__visited[v] = 0
            
            flow = self.DFS(s, t, float("inf"))
            # self.showGraph()
            while (flow > 0):
                total = total + flow
                # print(total)
                flow = self.DFS(s, t, float("inf"))
                # self.showGraph()

        return total

#######MAIN
def main():

    sample_min = 10
    sample_max = 500
    step = 25
    
    x = [i for i in range(sample_min, sample_max + 1, step)]
    
    e_k_algo = []
    dinics_algo = []
    p_r_algo = []
    
    for node_count in x:
        print("Processing", node_count, "x", node_count, "matrix now.")
        
        source_s = 0
        dest_d = node_count - 1

        G = Graph(node_count)
        Network = G.get_graph()
        
        #Edmonds-Karp
        time_taken = time.time()
        Edmonds_Karp(Network, source_s, dest_d)
        e_k_algo.append(time.time() - time_taken)       
        
        # #Push-Relabel
        time_taken = time.time()
        relabel_to_front(Network, source_s, dest_d)
        p_r_algo.append(time.time() - time_taken)
        
        # Dinic's 
        time_taken = time.time()
        G.DinicMaxFlow(source_s, dest_d - 1)
        dinics_algo.append(time.time() - time_taken)

    fig = plt.figure()
    algorithms = fig.add_subplot(111)

    algorithms.set_title('Algorithms Comparision (Adjacency Matrices) \nMatrix Orders: ' + str(sample_min)+ " to " + str(sample_max) + "\nSampling interval: " + str(step))
    algorithms.set_xlabel('matrix size (nXn)')
    algorithms.set_ylabel('time (seconds) ')
    
    algorithms.plot(x, p_r_algo,'o-' , color='yellow', label='Push-relabel algorithm O(V\N{SUPERSCRIPT TWO}E)')
    algorithms.plot(x, e_k_algo,'o-' , color='blue', label='Edmonds-karp algorithm O(VE\N{SUPERSCRIPT TWO})')
    algorithms.plot(x, dinics_algo, 'o-', color='red', label='Dinic\'s algorithm O(V\N{SUPERSCRIPT TWO}E)')
    
    algorithms.grid(linestyle='-')
    legend = algorithms.legend()
    
    plt.show()



if __name__ == '__main__':
    main()
