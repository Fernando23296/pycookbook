#in this case, deque is like a solid list, where the values added are going to move to the left

from collections import deque
q = deque(maxlen=3)
#in the maxlen we define the size
q.append(1)
q.append(2)
q.append(3)


print(q)
'''
________________________
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
________________________
'''
q.append(4)
print(q)
'''
________________________
|       |       |       |
|   2   |   3   |   4   |
|       |       |       |
________________________

the first value get removed

'''
q.append(5)
print(q)

#if you dont give it a maximum size, you get an UNBOUNDED queue
q= deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
#pop show and delete the last item
print(q.pop())
print(q)
print(q.popleft())
print(q)



