#플로이드 워셜 알고리즘

#무한을 의미
INF=int(1e9)

#노드 개수
n=int(input())

#간선 개수
m=int(input())

#2차원 리스트 만들고 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#간선 정보 입력받아 초기화
for _ in range(m):
    a,b,c=map(int,input().split())
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
            print('INFINITY',end=' ')
        else:
            print(graph[a][b],end=' ')
    print()
            
