n,m,k=map(int,input().split())

arr=list(map(int,input().split()))

arr.sort(reverse=True)
#첫번째로 큰 수
first=arr[0]
#두번째로 큰 수
second=arr[1]

#큰 수를 더하는 횟수
count=int(m/(k+1))*k
count+=m%(k+1)

#결과
result=0
result+=first*count
result+=second*(m-count)

print(result)
