#두 배열의 원소 교체
n,k=map(int,input().split())

#리스트 입력받기
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#a는 작은것부터 b는 큰것부터 정렬
a.sort()
b.sort(reverse=True)

#정렬된 a,b 확인하기
print(a)
print(b)

#앞에서부터 k번 순서대로 비교
for i in range(k):
    #a가 b보다 작으면 교체
    if a[i]<b[i]:
        tmp=a[i]
        a[i]=b[i]
        b[i]=tmp
    else:
        break

print(sum(a))
