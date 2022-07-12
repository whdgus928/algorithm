#최단경로 - 플로이드

#POINT
# 1. 입력데이터 100개 -> 플로이드 알고리즘 사용
# 2. 버스는 하나가 아닐수도 있음
# 3. 단방향
# 4. 시작도시와 도착 도시가 같은 경우는 없다


#플로이드 풀이순서
#무한 선언
#2차원 리스트 생성
#자기 자신으로 가는 비용 0으로 초기화
#간선 정보 받기
#플로이드 알고리즘 수행
#결과 출력

#무한을 의미
INF=int(1e9)

#도시 개수
n=int(input())

#버스 개수
m=int(input())

#2차원 리스트 만들고 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#POINT 4
#자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1,n+1):
    graph[i][i]=0

#버스 정보 입력받아 초기화
for _ in range(m):
    a,b,c=map(int,input().split())
    #POINT 2
    if graph[a][b]!=INF:
        if graph[a][b]<c:
            continue
    else:
        graph[a][b]=c

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print('0',end=' ')
        else:
            print(graph[a][b],end=' ')
    print()
