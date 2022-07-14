#크루스칼 알고리즘


#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트가 아니라면 루트 찾을때까지 재귀 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드 개수, 간선 개수 입력받기
v,e=map(int,input().split())
#부모 테이블 초기화
parent=[0]*(v+1)

#간선을 담을 리스트와 최종 비용 변수
edges=[]
result=0

#부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

#간선 정보 입력받기
for i in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()

#간선 하나씩 확인
for edge in edges:
    cost,a,b=edge
    #사이클이 발생하지 않은 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)

