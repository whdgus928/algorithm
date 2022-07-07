#바닥공사

n=int(input())

d=[0]*1001

#가로 1일때는 1가지
d[1]=1
#가로 2일때는 3가지
d[2]=3

for i in range(3,n+1):
    #식 이해x
    d[i]=(d[i-1]+2*d[i-2])%796796

print(d[n])
