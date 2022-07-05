#이진탐색 함수
def binary_search(array,target,start,end):
    while start<=end:
        # 소수점 버림
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        # 중간점 > target이면 끝점을 땡김
        elif array[mid]>target:
            end=mid-1
        # 중간점 < target이면 시작점을 땡김
        else:
            start=mid+1
    return None

n=int(input())
array=list(map(int,input().split()))
#이진탐색을 위한 정렬
array.sort()

m=int(input())
target_list=list(map(int,input().split()))

for i in target_list:
    result=binary_search(array,i,0,n-1)
    if result==None:
        print("no",end=' ')
    else:
        print('yes',end=' ')
