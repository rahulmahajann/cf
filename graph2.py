# bfs  --> traversing the adjacent nodes of graph at first!

def bfsgraph(n,adj[]):
    bfs=[]

    # visited array
    vis=[]
    for _ in range(n):
        vis.append(0)

    for _ in range(1,n+1):
        if(vis[_]==0):
            

# numbers of vertex and edge
n,e=map(int,input().split())

# creation of adjacency list!
adj=[]
for _ in range(n+1):
    adj.append([])

for _ in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

print('adjacency list: -->')
for _ in range(1,n+1):
    print(_,adj[_])




# 7 6
# 1 2
# 2 3
# 2 7
# 3 5
# 5 7
# 4 6