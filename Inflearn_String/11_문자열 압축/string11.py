import sys

input=sys.stdin.readline

text=input().strip()

n=len(text)


result=[]
count=1

for i in range(1,n):
  if text[i]==text[i-1]:
    count+=1
  else:
    result.append(text[i-1])
    if count != 1:
      result.append(str(count))
    count=1
print(result)
result.append(text[-1])
if count!= 1:
  result.append(str(count))
print(result)
print("".join(result))