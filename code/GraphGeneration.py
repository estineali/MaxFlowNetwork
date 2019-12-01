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
    
    capacity = GenerateGraph(size)
    
    showGraph(capacity)