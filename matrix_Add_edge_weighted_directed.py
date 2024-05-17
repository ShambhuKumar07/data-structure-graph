def add_node(v):
    global nodes_counts
    if v in nodes:
        print(v,"is already present in the nodes")
    else:
        nodes_counts +=1
        nodes.append(v)

        for n in graph:
            n.append(0)

        temp=[]
        for i in range(nodes_counts):
            temp.append(0)

        graph.append(temp)

def add_edge_Weighted_directed(v1,v2,count):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=count

def print_graph():
    for i in range(nodes_counts):
        for j in range(nodes_counts):
            print(format(graph[i][j],"<3"),end=" ")
        print()

nodes=[]
graph=[]
nodes_counts=0

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

print(nodes)

add_edge_Weighted_directed("A","G",10)
add_edge_Weighted_directed("D","G",20)
add_edge_Weighted_directed("D","C",30)
add_edge_Weighted_directed("B","F",40)
add_edge_Weighted_directed("G","B",50)

print_graph()