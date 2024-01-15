def ucs(graph, start, goals): 
    priority_queue = [(0, start)] 
    result = {} 
    while priority_queue: 
        priority_queue.sort() 
        current_cost, current_node = priority_queue.pop(0) 
        if current_node in goals: 
            result[current_node] = current_cost 
            goals.remove(current_node) 
            if not goals: 
                return result 
        for neighbor, edge_cost in graph[current_node].items(): 
            new_cost = current_cost + edge_cost 
            existing_neighbor_index = None 
            for i, (cost, node) in enumerate(priority_queue): 
                if node == neighbor: 
                    existing_neighbor_index = i 
                    break 
            if existing_neighbor_index is not None and priority_queue[existing_neighbor_index][0] > new_cost: 
                del priority_queue[existing_neighbor_index] 
            priority_queue.append((new_cost, neighbor)) 
    return None 

graph = { 
'A': {'B': 1, 'C': 4}, 
'B': {'G2': 3}, 
'C': {'G2': 1, 'E': 5}, 
'G2': {'E': 1}, 
'E': {'F': 2}, 
'F': {'G1': 3}, 
'G1': {} 
} 

start_node = 'A' 
goal_nodes = {'G1', 'G2'} 
results = ucs(graph, start_node, goal_nodes) 
if results: 
    for goal, cost in results.items(): 
        print(f"Shortest path cost from {start_node} to {goal}: {cost}") 
else: 
    print(f"No path found from {start_node} to any of the goal nodes") 

# visited = [] 
# queue = [] 

# def bfs(visited, graph, node): 
#     visited.append(node) 
#     queue.append(node) 
#     while queue: 
#         x = queue.pop(0) 
#         print(x, end=" ") 
        
#         for adj in graph[x]: 
#            if adj not in visited: 
#              visited.append(adj) 
#              queue.append(adj) 

# print("Following is BFS:") 
# bfs(visited, graph, '6') 

#using recursion 


