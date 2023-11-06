# DFS (1) [visited = ['A'], node = 'A', graph1]
# DFS (2) [visited = ['A','B'], node = 'B', graph1]
# X DFS (3) [visited = ['A','B'], node = 'A', graph1]
# DFS (4)[visited = ['A','B','D'], node = 'D', graph1]
# DFS (5) [visited = ['A','B','D','E'], node = 'E', graph1]
# DFS 

# if node not in visted. Base statment.

# Generate a random   graph with n nodes and m edges
# graph1 = {"A": set(["B", "C", "D"]), "B" : set(

graph1 = {
    "A" : set(["B", "C", "D"]),
    "B" : set(["E", "F"]),
    "C" : set(["A", "G", "H", "D"]),
    "D" : set(["A", "C","E","F","I"]),
    "E" : set(["B", "D", "I", "F", "H"]),
    "F" : set(["B", "D", "E", "I", "J"]),
    "G" : set(["C"]),
    "H" : set(["C", "E"]),
    "I" : set(["D", "E", "F"]),
    "J" : set(["F"])
}

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
        return visited

visited = dfs(graph1, "A", [])
print(visited)

