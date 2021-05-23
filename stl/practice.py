for _ in range(int(input())):
    g=list(map(int,input().split()))
    arr=g[2:len(g)]
    ans=0
    for _ in range(g[0],len(arr)):
        ans+=arr[_]
    print(ans)
    min=0
    