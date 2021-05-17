# n,e=map(int,input().split())

# adj=[]
# vis=[]
# for _ in range(n+1):
#     adj.append([])
#     vis.append(0)

# for _ in range(e):
#     u,v=map(int,input().split())
#     adj[u].append(v)
#     adj[v].append(u)

# que=[]

# def dfs(node,vis,adj,que):
#     que.append([node,prev])
#     vis[node]=1
#     for _ in adj[node]:
