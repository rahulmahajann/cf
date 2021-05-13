# detection of cycle in the undirected graph using breadth first search (bfs)

n,e=map(int,input().split())

adj=[]

for _ in range(n+1):
    adj.append([])

for _ in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

print(adj)


# input for number of nodes and edges of the graph
# 11 10

# input of u and v
# 1 2
# 2 4
# 3 5
# 5 6
# 6 7
# 7 8
# 5 10
# 10 9 
# 8 9
# 8 11


vis=[]

for _ in range(n+1):
    vis.append(0)

def cycleinbfs():
    print(1)

for _ in range(1,n+1):
    if(vis[_]==0):
        if(cycleinbfs(_)):
            print(1)