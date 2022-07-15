#그리디
#모험가 길드

n=int(input())
arr=list(map(int, input().split()))

#그룹 변수
count=0

#배열 정렬
arr.sort()

ad=[]
for i in arr:
    ad.append(i)
    if len(ad)>=i:
        count+=1
        ad=[]
   

print(count)
