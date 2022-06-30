# 맵 사이즈 입력받기
n,m=map(int,input().split())

#맵 정보 입력할 리스트 만들기
ice_map=[]

#맵 정보 입력받기
for i in range(n):
    ice_map.append(list(map(int,input())))

#얼음 개수 변수
result=0

# 해당좌표확인하고  상,하,좌,우 확인
def find(x,y):

    #맵에서 벗어났으면 탈출
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    #현재 좌표 방문x
    if graph[x][y]==0:
        graph[x][y]=1

        find(x-1,y)
        find(x+1,y)
        find(x,y+1)
        find(x,y-1)
        return True
    return False

#얼음지도에서 하나씩 탐색
for i in range(n):
    for i in range(m):
        if find(i,j)==True:
            result+=1

print(result)    
