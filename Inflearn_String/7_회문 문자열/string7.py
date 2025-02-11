import sys

input=sys.stdin.readline

str=input().strip()

str=str.upper()

if str==str[::-1]:
  print("YES")
else:
  print("NO")