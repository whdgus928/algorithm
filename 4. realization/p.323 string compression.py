def solution(s):
    answer=len(s)

    #압축 단위 하나씩 증가
    for unit in range(1,len(s)//2+1):
      compressed=''
      #비교대상
      pre=s[0:unit]
      count=1

      #압축 단위 별로 비교
      for j in range(unit,len(s),unit):
        if pre==s[j:j+unit]:
          count+=1
        #비교해서 다르면 압축 문자 입력하고 비교대상 문자열 교체
        else:
          compressed+=str(count)+pre if count>=2 else pre
          pre=s[j:j+unit]
          count=1
      #남아있는 문자열 처리
      compressed+=str(count)+pre if count>=2 else pre 
      answer=min(answer,len(compressed))

    return answer
