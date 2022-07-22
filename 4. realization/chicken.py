from itertools import combinations

n,m=map(int,input().split())

chicken,house=[]

for i in range(n):
    data=list(map(int,input().split()))
    for c in range(n):
        if data[c]==1:
            house.append(i,c)
        elif data[c]==2:
            chicken.append(i,c)

survived=list(combinations(chicken,m))


def distance()
for hx,hy in house:
    for cx,cy in chicken:
        
