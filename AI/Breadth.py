# We will do 3 dry runs 

'''
graph = {'A': set(['B', 'C']),
'B': set(['A', 'D', 'E']),
'C': set(['A', 'F']),
'D': set(['B']),
'E': set(['B', 'F']),
'F': set(['C', 'E'])
}
'''

# Dry run for bfs algorithm:

# BFS(1) [visited=['A'], levels={'A': 0}, queue=['A'], start='A']

# BFS(2) [visited=['A'], levels={'A': 0}, queue=[], node='A', neighbours=['B','C'], graph=graph]
# BFS(3) [visited=['A', 'B'], levels={'A': 0, 'B': 0}, queue=['B'], node='A', neighbour='B']
# BFS(3) [visited=['A', 'B', 'C'], levels={'A': 0, 'B': 0, 'C': 0}, queue=['B', 'C'], node='A', neighbour='C']

# BFS(4) [visited=['A', 'B', 'C'], levels={'A': 0, 'B': 0, 'C': 0}, queue=['C'], node='B', neighbours=['A','D','E'], graph=graph]
# X BFS(5) [visited=['A', 'B', 'C'], levels={'A': 0, 'B': 0, 'C': 0}, queue=['C'], node='B', neighbour=['A']]
# BFS(5) [visited=['A', 'B', 'C', 'D'], levels={'A': 0, 'B': 0, 'C': 0, 'D': 1}, queue=['C', 'D'], node='B', neighbour=['D']]
# BFS(5) [visited=['A', 'B', 'C', 'D', 'E'], levels={'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1}, queue=['C', 'D', 'E'], node='B', neighbour=['E']]

# Dry run for bfs_paths algorithm:

# BFSP(1) [goal='F', start='A', graph=graph, queue=[('A', ['A'])] ]

# BFSP(2) [goal='F', start='A', graph=graph, vertex='A', path=['A'], queue=[] ]
# BFSP(2) [goal='F', start='A', graph=graph, vertex='A', path=['A'], next='B', graph[vertex] - set(path)=['B','C'] queue=[('B', ['A', 'B'])] ] #Performing set difference
# BFSP(2) [goal='F', start='A', graph=graph, vertex='A', path=['A'], next='C', graph[vertex] - set(path)=['B','C'] queue=[('B', ['A', 'B']), ('C', ['A', 'C'])] ] #Performing set difference

# BFSP(3) [goal='F', start='A', graph=graph, vertex='B', path=['A', 'B'], queue=[('C', ['A', 'C'])]]
# BFSP(3) [goal='F', start='A', graph=graph, vertex='B', path=['A', 'B'], next='D', graph[vertex] - set(path)=['D','E'] queue=[('C', ['A', 'C']), ('D', ['A','B','D'])] ] #Performing set difference
# BFSP(3) [goal='F', start='A', graph=graph, vertex='B', path=['A', 'B'], next='E', graph[vertex] - set(path)=['D','E'] queue=[('C', ['A', 'C']), ('D', ['A','B','D']), ('E', ['A','B','E'])] ] #Performing set difference

# BFSP(4) [goal='F', start='A', graph=graph, vertex='C', path=['A', 'C'],  queue=[('D', ['A','B','D']), ('E', ['A','B','E'])] ]
# BFSP(4) [goal='F', start='A', graph=graph, vertex='C', path=['A', 'C'], next='F', graph[vertex] - set(path)=['F'] queue=[('D', ['A','B','D']),  ('E', ['A','B','E'])] ] #Performing set difference
# yeilds ['A', 'C', 'F']

# Dry run for shortest_path algorithm:

# just prints the first result from bfs_paths (using next()) which inherently would be the shortest path
# breadth wise search would add solutions in ascending order of levels of node.

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

def bfs(start, graph):
    queue = [start]
    levels = {start: 0}
    visited = [start]
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                levels[neighbour] = levels[node] + 1

    return levels
print(bfs('A', graph1))

def bfs_paths(start, goal, graph):
    queue = (start, [start])
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):