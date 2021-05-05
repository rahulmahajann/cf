# dfs in graph 
# deapth first search

n,e=map(int,input().split())

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
    