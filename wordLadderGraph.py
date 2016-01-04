import sys
import networkx as nx 
g = nx.Graph()
gdict = {}
if len(sys.argv) >= 2:
	args = sys.argv
	start = args[1]
	end = args[2]

with open('../lenSortedEngWords.txt') as inputfile:
			for line in inputfile:
				word = line[:-1]
				if len(word)==1:
					gdict[word]=[]
				else:
					gdict[word]=[]
					for i in range(len(word)):
						sub = word[:i] + "" + word[i+1:]
						if sub in gdict:
							#gdict[sub].append(word)
							g.add_edge(sub, word)
						else:
							g.add_node

# for root in gdict:
# 	if len(gdict[root])>= 1:
# 		#print root, gdict[root]
# 		for node in gdict[root]:
# 			g.add_edge(root, node)
# 	else:
# 		g.add_node(root)


if nx.has_path(g, start, end):
	for p in nx.all_shortest_paths(g, start, end):
		print p, len(p)
else:
	print "none"