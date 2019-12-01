from GraphGeneration import *

def BFS(G, source):
    #initialization
    visited = [False for i in range(len(G))] #visited List 
    Qu = list() #Temporary Queue to keep track of nodes in breadth 
    track = list() #Containing nodes in order of visit 
    
    #set source as the begining of the search
    Qu.append(source) 
    visited[source] = True

    while Qu:
        print(Qu) #state of visiting 
        v = Qu.pop(0)
        track.append(v)
        for i in range(len(G[v])):
            if G[v][i] != 0 and visited[i] == False:
                Qu.append(i)
                visited[i] = True
    
    print(track)
    
    return track

size = 10
# source_s = random.randint(0, size)
source_s = 0

Network = GenerateGraph(size)

showGraph(Network)

BFS(Network, source_s)