n=int(input('숫자 입력: '))
array=list(map(int,input()))

array.reverse()

#dp n만큼 초기화
dp=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i]=max(dp[i],dp[j]+1)


print(n-max(dp))

