def dfs(graph, start, visited=None):
    if visited is None:
        visited = set() 
    
    print(start, end=' ')  
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("DFS traversal starting from vertex A:")
    dfs(graph, 'A')
