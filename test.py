import networkx as nx
G=nx.Graph()
G=nx.complete_graph(100)
G=nx.star_graph(10)
G.add_node("spam")
G.add_edge(1,2)
G.add_edge(1,6)
G.add_edge(5,8)
G.add_edge(5,9)
G.add_edge(7,9)
G.add_edge(3,8)
print(G.nodes())
print(G.edges())
