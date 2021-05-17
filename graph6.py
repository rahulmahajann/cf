# check whether it is a bipartite graph or not (bfs use)

# it isn't a bipartite graph

# 8 8
# 1 2
# 2 3
# 3 4
# 4 5
# 5 8
# 2 8
# 5 6
# 6 7


# it's a bipartite graph

# 8 8
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6
# 6 7
# 2 7
# 5 8


n,e=map(int,input().split())

clr=[]
adj=[]

for _ in range(n+1):
    adj.append([])
    clr.append(0)

for _ in range(e):
    u,v=map(int,input().split())
    adj[v].append(u)
    adj[u].append(v)

que=[]

def bipar(strt,adj,clr):
    que.append(strt)
    clr[strt]='a'
    while(len(que)!=0):
        node=que[0]
        que.pop(0)

        for _ in adj[node]:
            if(clr[_]==0 and clr[node]=='a'):
                clr[_]='b'
                que.append(_)
            elif(clr[_]==0 and clr[node]=='b'):
                clr[_]='a'
                que.append(_)
            elif(clr[_]==clr[node]):
                return 0
    return 1

for _ in range(1,n+1):
    if(clr[_]==0):
        if(bipar(_,adj,clr)==0):
            print('no it is not a bipartite graph')
            break
        else:
            print('it is a bipartite graph!')
            break

        