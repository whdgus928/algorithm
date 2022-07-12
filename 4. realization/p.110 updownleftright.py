#상하좌우
#구현

#공간 크기
n=int(input())

# 이동할 계획
move_list=list(input().split())

#첫 좌표
x,y=1,1
nx,ny=0,0

#이동방식 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]
dir=['U','D','L','R']

#이동
for move in move_list:
    for i in range(4):
        if dir[i]==move:
            nx=x+dx[i]
            ny=y+dy[i]
            print(x,y)
        if nx>n or nx<1 or ny>n or ny<1:
            continue
        x,y=nx,ny

print(x,y)
    
