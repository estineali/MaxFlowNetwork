import random

def GenerateGraph(lengthG):
    #Generate adjacency (Capacity) matrix of order lengthG
    random.seed(100)
    G = [[0 for i in range(lengthG)] for j in range(lengthG)]
    for i in range(lengthG):
        for j in range(len(G[i])):
            capacity = random.randint(-20, 15)
            if capacity > 0 and j != i:
                G[i][j] = capacity
    return G

def GenerateNetwork(lengthG):
    #Generate adjacency (Capacity) matrix of order lengthG with a sink
    random.seed(100)
    G = [[0 for i in range(lengthG)] for j in range(lengthG)]
    for i in range(lengthG):
        for j in range(len(G[i])):
            capacity = random.randint(-20, 15)
            if capacity > 0 and j != i and j != 0:
                if G[j][i] == 0:
                    G[i][j] = capacity
    return G

def GenerateNeighbourMatrix(G):
    E = list()
    for i in G:
        neighbours = []
        for j in range(len(i)):
            if i[j] > 0:
                neighbours.append(j)
        E.append(neighbours.copy())
        neighbours.clear()
    return E

def showGraph(G):
    for i in range(len(G)):
        print(i, ":", G[i])

def pushToFile(G):
    file_f = open("graphs.txt", 'a')

    file_f.write("\nBegin Graph\n")
    
    for i in range(len(G)):
        #make each entry a string.
        #Then merge into 1 comma sep. string
        s = ", ".join( [str(j) for j in G[i]] )  
        file_f.write(s + "\n") # write to file. Move cursor to next line 

    file_f.write("End Graph\n")
    
    file_f.close()

if __name__ == '__main__':
    print("Graph Generation Library")
    print("Test Driver:")

    size = 6 
    
    Graph_G = GenerateGraph(size)
    
    showGraph(Graph_G)

    Neighbours_N = GenerateNeighbourMatrix(Graph_G)

    showGraph(Neighbours_N)