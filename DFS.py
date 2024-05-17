def create_vertex(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")

    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(vertext,visited,graph):
    if vertext not in graph:
        print("Vertext not present in the graph")
        return
    if vertext not in visited:
        print(vertext,end=" ")

        visited.add(vertext)

        for i in graph[vertext]:
            DFS(i,visited,graph)


graph={}

visited=set()

create_vertex(0)
create_vertex(1)
create_vertex(2)
create_vertex(3)
create_vertex(4)
create_vertex(5)
create_vertex(6)

print("Vertexts:",graph)

add_edge(0,1)
add_edge(0,2)
add_edge(1,3)
add_edge(1,4)
add_edge(2,1)
add_edge(2,5)
add_edge(3,6)

print("Edges:",graph)

print("Depth First Search")

DFS(0,visited,graph)
print()