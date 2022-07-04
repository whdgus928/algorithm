n=int(input())

house=[]

sum2=0

for i in range(n):
    house.append(list(map(int,input())))

house.sorted(house)

for i in range(n):
    for j in house:
        sum=0
        sum+=abs(i-j)
        sum2=sum


#간단 풀이
n=int(input())
for i in range(n):
    house.append(list(map(int,input())))

house.sort()

print(house[(n-1)//2])
