# bfs  --> traversing the adjacent nodes of graph at first!

# def bfsgraph(n,adj[]):
#     bfs=[]

#     # visited array
#     vis=[]
#     for _ in range(n):
#         vis.append(0)

#     for _ in range(1,n+1):
#         if(vis[_]==0):
            

# numbers of vertex and edge
n,e=map(int,input().split())

# creation of adjacency list!
adj=[]
for _ in range(n+1):
    adj.append([])

print(adj)

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

que=[]
ans=[]

for _ in range(1,n+1):
    if(vis[_]==0):
        que.append(_)
        vis[_]=1
        while(len(que)!=0):
            node=que[0]
            que.remove(node)
            ans.append(node)

            for i in adj[node]:
                if(vis[i]==0):
                    que.append(i)
                    vis[i]=1



print(ans)

# 7 6
# 1 2
# 2 3
# 2 7
# 3 5
# 5 7
# 4 6


# steps followed


# 1. create a adjacency list!
# 2. then create a visited array
# 3. take 2 list que and ans
# 4. iterate all of the vertices from 1 to n
# 5. check if the vertex is visited or not. If not visited then continue
# 6. then follow the above algorithm!