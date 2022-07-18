n=input()

#중간지점 구하기
point=len(n)//2

#왼쪽 합
totalleft=0
#오른쪽 합
totalright=0

#왼쪽 합 구하기
for i in range(point):
    totalleft+=int(n[i])

#오른쪽 합 구하기
for i in range(point,len(n)):
    totalright+=int(n[i])

#합 비교
if totalleft==totalright:
    print('Lucky')
else:
    print('Ready')
