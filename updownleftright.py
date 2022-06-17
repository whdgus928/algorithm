#시뮬레이션, 구현, 완전 탐색 유형

n=int(input())
#출발위치
x,y=1,1
plans=input().split()

# 동,서,남,북에 따른 이동 방향
dx=[1,-1,0,0]
dy=[0,0,-1,1]
move_types=['R','L','S','w']

for plan in plans:
    for i in range(len(move_types)):
        if plan==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or ny<1 or nx>n or nx>n:
        continue

    x=nx
    y=ny

print(x,y)
