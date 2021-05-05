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

vis=[]
for _ in range(n+1):
    vis.append(0)

print(vis)

ans=[]

def dfs(node,vis,adj,que):
    ans.append(node)
    vis[node]=1
    for _ in adj[node]:
        if(vis[_]==0):
            dfs(_,vis,adj,que)

for _ in range(1,n+1):
    if(vis[_]==0):
        dfs(_,vis,adj,ans)

print(ans)