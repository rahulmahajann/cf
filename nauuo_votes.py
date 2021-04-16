a,b,c=map(int,input().split())

if(c==0):
    if(a>b):
        print('+')
    elif(a<b):
        print('-')
    else:
        print('0')
elif(a==b):
    print('?')
else:
    if(a-b < 0 and abs(a-b) > c):
        print('-')
    elif(a-b > 0 and abs(a-b) > c):
        print('+')
    else:
        print('?')
        