n, d = map(int, input().split())
m = int(input())

if n >= 2 * d:
    for i in range(m):
        found = False
        x, y = map(int, input().split())
        if 0 <= x and x <= d and d - x <= y and x + d >= y:
            found = True
        if d <= x and x <= n - d and x - d <= y and x + d >= y:
            found = True
        if n - d <= x and x <= n and x - d <= y and -x + 2 * n - d >= y:
            found = True

        if found:
            print('YES')
        else:
            print('NO')
else:
    for i in range(m):
        found = False
        x, y = map(int, input().split())
        if 0 <= x and x <= n - d and d - x <= y and x + d >= y:
            found = True
        if n - d < x and x <= d and d - x <= y and -x + 2 * n - d >= y:
            found = True
        if d < x and x <= n and x - d <= y and -x + 2 * n - d >= y:
            found = True

        if found:
            print('YES')
        else:
            print('NO')
