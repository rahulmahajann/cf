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


