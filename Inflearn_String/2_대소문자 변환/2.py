import sys

input=sys.stdin.readline().strip

word=input()

# answer=[]
# for i in word:
#   if i.islower()==True:
#     answer.append(i.upper())
#   else:
#     answer.append(i.lower())

# for j in answer:
#   print(j,end='')

print(word.swapcase())