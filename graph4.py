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

que=[[0,1]]

def cycleinbfs(_):
    que.append([_,-1])
    vis[_]=1
    while(len(que)!=0):
        node = que[0][0]
        prev = que[0][1]
        que.pop(0)
        for _ in (adj[node]):
            if(vis[_]==1):
                if(_ == prev or _ == -1):
                    return False
                else:
                    return True

for _ in range(1,n+1):
    if(vis[_]==0):
        if(cycleinbfs(_)):
            print(1)
        else:
            print(0)

