import random

def GenerateGraph(lengthG):
    #Generate adjacency matrix of size lengthG x lengthG 
    random.seed(100)
    G = [[0 for i in range(lengthG)] for j in range(lengthG)]
    for i in range(lengthG):
        for j in range(len(G[i])):
            capacity = random.randint(-20, 15)
            if capacity > 0 and j != i:
                G[i][j] = capacity
    return G

def showGraph(G):
    for i in range(len(G)):
        print(i, ":", G[i])

size = 6 #change this 

capacity = GenerateGraph(size)
showGraph(capacity)
