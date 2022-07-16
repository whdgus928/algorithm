#그리디
#볼링공 고르기

n,m=map(int,input().split())

k=list(map(int,input().split()))

count=0

for i in range(0,len(k)-1):
    for j in range(i+1,len(k)):
        if k[i]!=k[j]:
            count+=1

print(count)
