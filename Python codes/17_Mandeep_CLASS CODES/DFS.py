def dfs(graph,root):
    visited,stack=set(),[root]    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            stack.extend(graph[vertex])
            
graph={0:[2,6],1:[0,3,4,6],2:[0,5,6,7],3:[1,4],4:[1,3,7],5:[2,6,7],6:[1,2,5],7:[5,4,2]}
dfs(graph,1)    