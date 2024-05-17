def create_node(v):
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
        # list1=[v2,cost]
        # list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

graph={ }

# create_node("A")
# create_node("B")
# create_node("C")
# create_node("D")

# add_edge("A","B")
# add_edge("A","C")
# add_edge("A","D")

create_node(0)
create_node(1)
create_node(2)
create_node(3)
# create_node("D")
add_edge(1,2)
add_edge(1,3)

# add_edge(0,2)
add_edge(0,2)
# add_edge(1,2)
# add_edge(2,0)
add_edge(0,1)

print(graph)