a=input()
b=input()


#편집 거리
result=0

point=0

if len(a)<len(b):
    #불가피한 삽입
    result+=len(b)-len(a)

for i in range(len(a)):
    if a[i] in b[point:]:
        point=b.index(a[i])+1
    else:
        result+=1

print(result)
