import sys

input=sys.stdin.readline

N=int(input().strip())

# words=[input().strip() for _ in range(N)]

# for i in words:
#   answer=i[::-1]
#   print(answer)

for _ in range(N):
  word = input().strip()
  print(word[::-1])