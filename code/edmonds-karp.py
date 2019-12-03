import math
from GraphGeneration import *
import matplotlib.pyplot as plt
import time 

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

def main():

	min_sample = 1
	max_sample = 2000
	x, y = [i for i in range(min_sample, max_sample + 1, 20)], []
	for node_count in x:
		print(node_count)
		source_s = 0
		dest_d = node_count - 1

		Network = GenerateNetwork(node_count)

		time_taken = time.time()
		
		max_flow = Edmonds_Karp(Network, source_s, dest_d)
		print(max_flow)
		time_taken = time.time() - time_taken
		
		y.append(time_taken * 1000)

	fig = plt.figure()
	E_K_algo = fig.add_subplot(111)
	
	E_K_algo.set_xlabel('matrix size (nXn)')
	E_K_algo.set_ylabel('time (milliseconds)')
	
	E_K_algo.plot(x, y, 'o-',color='red', label='Edmonds-Karp O(VE\N{SUPERSCRIPT TWO})')
	E_K_algo.grid(linestyle='-')
	
	legend = E_K_algo.legend()
	
	plt.show()

if __name__ == '__main__':
	main()
