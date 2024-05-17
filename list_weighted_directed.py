def create_node(v):
    if v in graph:
        print(v,"is already present ")
    else:
        graph[v]=[]

def add_edge_weighted(v1,v2,cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")

    else:
        list1= [v2,cost]

        graph[v1].append(list1)

graph={}


create_node(1)
create_node(2)
create_node(3)
create_node(4)

print("Graph",graph)

add_edge_weighted(1,2,"A")
add_edge_weighted(1,3,"B")
add_edge_weighted(2,3,"C")

add_edge_weighted(2,4,"D")

print("Undirected Weighted Graph",graph)