import random
import time as t

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
		# 						[0, 0,2,4,8, 0],
		# 						[0, 0,0,0,9, 0],
		# 						[0, 0,0,0,0, 10],
		# 						[0, 0,0,6,0, 10],
		# 						[0, 0,0,0,0, 0]]


		self.__G = [[0 for i in range(V)] for j in range(V)]
		for i in range(V):
			for j in range(V):
				C = random.randint(-20, 15)
				if C > 0 and j != i:
					self.__G[i][j] = C


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

G =  Graph(6) # Graph(V) forms V x V matrix
t0 = t.clock()
print(G.DinicMaxFlow(0, 5))  
t1 = t.clock() 
print( "Time in milliseconds: ", t1 - t0) # Time for algorithm to run















