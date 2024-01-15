import networkx as nx
import heapq  


graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

G = nx.Graph()
for node, edges in graph.items():
    G.add_node(node)
    for neighbor, weight in edges:
        G.add_edge(node, neighbor, weight=weight)

# Input the heuristic values
h = {
    'A': 11,
    'B': 6,
    'C': 99,
    'G': 0,
    'E': 7,
    'D': 1
}


def a_star_algorithm(start, stop):
    open_list = [(0, start)]  
    came_from = {}  
    g_score = {node: float('inf') for node in G.nodes}  # Initialize g_scores to infinity
    g_score[start] = 0  # Start node has a g_score of 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == stop:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            print('Path found:', path)
            return path

        for neighbor in G.neighbors(current):
            tentative_g_score = g_score[current] + G.get_edge_data(current, neighbor).get('weight', 0)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current   
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h.get(neighbor, 0)
                heapq.heappush(open_list, (f_score, neighbor))

    print('Path does not exist!')
    return None


start_node = 'A'
goal_node = 'G'
path = a_star_algorithm(start_node, goal_node)