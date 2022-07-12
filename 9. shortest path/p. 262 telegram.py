#다익스트라 알고리즘
#n,m의 범위가 크므로 우선순위 큐 이용한 다익스트라 사용

import heapq
import sys

#더 빠르게 데이터 읽음
input=sys.stdin.readline
#무한을 의미
INF=int(1e9)

#노드 개수, 간선 개수, 시작 노드
n,m,start=map(int,input().split())

#노드 정보 담을 리스트 만들기
graph=[[] for i in range(n+1)]

#최단 거리 테이블 무한으로 초기화
distance=[INF]*(n+1)

#간선 정보 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())

    graph[a].append((b,c))

#다익스트라 알고리즘
def dijkstra(start):
    q=[]
    
    #시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    #큐가 비어있지 않다면
    while q:
        dist,now=heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost=dist+i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
#다익스트라 실행
dijkstra(start)

#도달할 수 있는 노드 개수
count=0

# 최단거리 출력
max_distance=0
for i in distance:
    #도달할 수 있으면
    if d!==INF:
        count+=1
        max_distance=max(max_distance,i)

#시작 노드는 제외
print(count-1, max_distance)
