#https://www.tutorialspoint.com/execute_python_online.php

class Node:
	rotulo = ""

	def __init__(self, string):
		self.rotulo = string
		
class Edge:
		arco = []

		def __init__(self,nodeA,nodeB,peso):
			self.arco = [nodeA,nodeB,peso]

class Graph:
	edges = []
	vertices = []
	
	def insert_node(self, node):
		self.vertices.append(node)
	
	def insert_node_by_rotulo(self, rotulo):
		if [i for i in self.vertices if i.rotulo == rotulo] :
			return false
		else :
			insert = Node(rotulo)
			self.insert_node(insert)
		  return true	
	
	def insert_nodes(self, rotulos):
		for rotulo in rotulos:
			self.insert_node_by_rotulo(rotulo)
			
			
first = Node("Raiz")
first.insereAdj("second", 5)
first.insereAdj("third", 6)
first.insereAdj("fourth", 1)
first.printAdjs()

print(any("second" in s for s in first.adjacencias))
matching = [s for s in first.adjacencias if "second" in s]
print(matching)
