a=[]

n,e=map(int,input().split())

for i in range(n+1):
    a.append([])

# print(a)

for _ in range(e):
    u,v,wt=map(int,input().split())
    a[u].append([v,wt])
    a[v].append([u,wt])

print(a)

# 5 7
# 1 5 0
# 5 3 2
# 1 3 3
# 1 2 2
# 2 3 4
# 3 4 1
# 4 2 5