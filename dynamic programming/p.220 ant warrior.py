#개미전사, 바텀업

n=int(input())

array=list(map(int,input().split()))

#테이블 초기화
d=[0]*100

#경우의 수 1가지
d[0]=array[0]

#경우의 수 2가지
d[1]=max(array[0],array[1])


for i in range(2,n):
    d[i]=max(d[i-1],d[i-1]+array[i])

print(d[n-1])
