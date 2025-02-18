import sys

input=sys.stdin.readline

str=input().strip()

answer=[]
for i in str:
  if i.isdigit():
    answer.append(i)
print(int(''.join(answer)))