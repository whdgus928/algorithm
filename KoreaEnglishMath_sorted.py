n=int(input())

array=[]
for i in range(n):
    data=input().split()
    array.append((data[0],int(data[1]),int(data[2]),int(data[3])))

#- 내림차순, + 오름차순
array.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in array:
    print(student[0])
