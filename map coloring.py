print("Map Coloring")
def is_valid_coloring(graph, node, color, coloring):
    for neighbor in graph[node]:
        if coloring[neighbor] == color:
            return False
    return True
#coloring: Represents the current coloring of the nodes. It's a list where the index corresponds to the node number,
# and the value corresponds to the color assigned to that node.
#node: Represents the current node being considered for coloring.
def map_coloring(graph, colors, coloring, node):
    if node == len(graph):
        return True  
    for color in colors:
        if is_valid_coloring(graph, node, color, coloring):
            coloring[node] = color
            if map_coloring(graph, colors, coloring, node + 1):
                return True
            coloring[node] = None
    return False
def solve_map_coloring(graph, colors):
    num_nodes = len(graph)
    coloring = [None] * num_nodes
    print(coloring)
    if map_coloring(graph, colors, coloring, 0):
        return coloring
    return None
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
print("graph:",graph)
colors = ['Red', 'Green', 'Blue']
coloring = solve_map_coloring(graph, colors)
if coloring:
    for node, color in enumerate(coloring):
        print(f"Node {node}: {color}")
else:
    print("No solution found.")