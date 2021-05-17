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

