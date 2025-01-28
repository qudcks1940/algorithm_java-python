import sys
import string

input=sys.stdin.readline

input1=input().strip()
input2=input().strip()

word=input1.lower()
letter=input2.lower()

count=0
for i in word:
  if i==letter:
    count+=1

print(count)