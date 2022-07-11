#미래도시
#플로이드 워셜 알고리즘
#2차원 리스트 생성
#자기 자신으로 가는 비용 0으로 초기화
#간선 정보 받기
#플로이드 알고리즘 수행
#결과 출

#무한을 의미
INF=int(1e9)

#회사 개수, 경로의 개수
n,m=map(int,input().split())

#2차원 리스트 만들고 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#간선 정보 입력
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1


#2번째 들릴 회사, 1번째 들릴 회사
x,k=map(int,input().split())

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

#1 -> k -> x 경로 구하기
distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance)
