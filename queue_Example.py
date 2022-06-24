from collections import deque #시간 복잡도 절약 가능

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
qeeue.popleft()
queue.append(1)
queue.append(4)
qeeue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue)
