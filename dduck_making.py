#떡볶이 떡 만들기(파라메트릭 서치 유형)
n,m=map(int,input().split())

dduck=list(map(int,input().split()))

start=0
end=dduck[len(dduck)-1]

while start<=end:
       mid=(start+end)//2
       for i in dduck:
           if i>mid:
               total+=i-mid
        if total<m:
            end=mid-1
        else:
            result=mid
            start=mid+1

print(result)
