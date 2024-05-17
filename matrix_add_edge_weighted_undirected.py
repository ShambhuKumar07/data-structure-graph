def add_nodes(v):
    global nodes_cunts
    if v in nodes:
        print(v,"is already present in nodes")

    else:
        nodes_cunts +=1
        nodes.append(v)

        for n in graph:
            n.append(0)
        
        temp=[]
        for i in range(nodes_cunts):
            temp.append(0)
        graph.append(temp)

def Add_edge_Weighted(v1,v2,count):
    if v1 not in nodes:
        print(v1,"is not present in the graph")
    elif v2 not in nodes:
        print(v2,"is not present in the graph")

    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)

        graph[index1][index2]=count
        graph[index2][index1]=count

def print_graph():
    for i in range(nodes_cunts):
        for j in range(nodes_cunts):
            print(graph[i][j],end=" ")
        
        print()

nodes=[]
graph=[]
nodes_cunts=0

add_nodes("A")
add_nodes("b")
add_nodes("c")
add_nodes("d")
add_nodes("e")

print(nodes)
# print(graph)
Add_edge_Weighted("A","b",4)
Add_edge_Weighted("b","c",7)

print_graph()