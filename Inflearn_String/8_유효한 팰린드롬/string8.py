# import sys

# input=sys.stdin.readline

# str=input().strip().split()

# answer=""
# for i in str:
#   for j in i:
#     if 'a'<=j<='z' or 'A'<=j<='Z':
#       answer+=j
# answer=answer.upper()

# if answer==answer[::-1]:
#   print("YES")
# else:
#   print("NO")

import sys

input=sys.stdin.readline

str=input().strip()

ans=""

left=0
right=len(str)-1

while(left<right):
  while left<right and not str[left].isalpha():
    left+=1
  while left<right and not str[right].isalpha():
    right-=1
  if left<right:
    if str[left].lower() != str[right].lower():
      ans="NO"
    left+=1
    right-=1
  ans="YES"
print(ans)