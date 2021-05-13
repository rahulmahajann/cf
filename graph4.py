# is there any cycle in the graph or not? using bfs

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


n,e=map(int,input().split())

adj=[]
vis=[]

for _ in range(n+1):
    adj.append([])
    vis.append(0)

for _ in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

# print('adjacency list: -->')

# for _ in range(1,n+1):
#     print(_,adj[_])
# print(adj)

que=[]
print('ans')
def cycleinbfs(_):
    que.append([_,-1])
    vis[_]=1
    while(len(que)!=0):
        node=que[0][0]
        prev=que[0][1]
        que.pop(0)
        for _ in adj[node]:
            if(vis[_]==0):
                que.append([_,node])
                vis[_]=1
            else:
                if(_ != prev):
                    return True
    return False

for i in range(1,n+1):
    if(vis[i]==0):
        if(cycleinbfs(i)):
            print('yes there is a cycle!')
            break
