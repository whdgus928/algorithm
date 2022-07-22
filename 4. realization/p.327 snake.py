#보드의 크기
n=int(input())
#사과의 개수
k=int(input())

#지도 리스트 - 아무것도 없으면 0, 사과 있으면 1, 뱀 있으면 -1
map=[[0]*(n+1) for _ in range(n+1)]

#방향 리스트
dir=[]

#사과 위치 받기
for _ in range(k):
    x,y=map(int,input().split())
    map[x][y]=1

#뱀의 방향 변환 횟수
l=int(input())
#방향 정보 입력
for _ in range(l):
    x,c=input().split()
    dir.append(int(x),c)

#동,남,서,북
dx=[0,1,0,-1]
dy=[1,0,-1,0]


