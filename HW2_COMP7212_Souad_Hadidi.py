import networkx as nx
from matplotlib import pyplot as plt

import random

def display(G):
	nx.draw(G)
	plt.savefig("simple_path.png") # save as png
	plt.show() # display

def addNode(G):
	newID = random.randint(1, 12)
	currIDList = list(G.nodes)
	if newID != currIDList:
		G.add_node(newID)
		print(G.has_succ(0))

G=nx.Graph()
G.add_node(0)

graphing = True
while graphing:
	print("To add a node, press 1")
	print("To remove a node, press 2")
	print("To view graph, press 3")
	print("To exit, press 0")
	val = int(input())
	if val == 3:
		display(G)
	elif val == 2:
		pass
	elif val == 1:
		addNode(G)

	elif val == 0:
		graphing = False
	else:
		pass
exit()
