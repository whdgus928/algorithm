#상하좌우
#구현

#공간 크기
n=int(input())

# 이동할 계획
move_list=list(input().split())

#첫 좌표
x,y=1,1

#상하좌우 방향설정
dx=[-1,1,0,0]
dy=[0,0,-1,1]
dir=['U','D','L','R']

#move_list 체크해서 하나씩 이동
for move in move_list:
    #dir 개수만큼
    for i in range(4):
        #move_list와 dir 비교해서 일치하는 방향으로 이동
        if dir[i]==move:
            nx=x+dx[i]
            ny=y+dy[i]
            print(x,y)
        #지도를 넘어가면 움직임 무시
        if nx>n or nx<1 or ny>n or ny<1:
            continue
        #지도를 넘어가지 않았다면 움직임 대입
        x,y=nx,ny

print(x,y)
    
