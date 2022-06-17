#완전탐색 문제(brute forcing) 가능한 모든 경우의 수 탐색
#3 들어간 시간 체크

n=int(input())

count=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1


print(count)
