import sys

input=sys.stdin.readline

str=input().strip()

s=set()

result=""
for i in str:
  if i in s:
    pass
  else:
    s.add(i)
    result+=i
print(result)