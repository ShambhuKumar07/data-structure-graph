def add_node(v):
    global node_counts

    if v in nodes:
        print(v, "is already present")
    else:
        node_counts +=1
        nodes.append(v)
        
        for n in graph:
            n.append(0)

        temp=[]
        for i in range(node_counts):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=1
        graph[index2][index1]=1 

def print_graph():
    for i in range(node_counts):
        for j in range(node_counts):
            print(graph[i][j],end=" ")

        print()

nodes=[]
graph=[]
node_counts=0

add_node("A")
add_node("b")
add_node("c")
add_node("d")
add_node("e")

print(nodes)
# print(graph)
add_edge("A","b")

print_graph()