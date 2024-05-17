def add_node(v):
    global node_count
    if v in nodes:
        print(v," is Already present")
    else:
        node_count +=1
        nodes.append(v)
        for n in graph:
            n.append(0)

        temp=[]

        for i in range(node_count):
            temp.append(0)

        graph.append(temp)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")

        print()
nodes=[]
graph=[]
node_count=0

add_node("A")
add_node("b")
add_node("c")
add_node("d")
add_node("e")

print(nodes)
# print(graph)

print_graph()