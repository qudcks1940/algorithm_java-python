# 나는 투포인터를 활용해서 양쪽 다 문자이면 서로 바꾸고,
# 하나라도 문자가 아니라면 바꾸지 않는 방식으로 코드를 짰는데,
# GPT가 추천한 코드는 우선 알파벳만 다 뽑은 뒤에
# 원래 문자열에서 문자면 뒤에서부터 순서대로 넣는 방식이다.

# GPT가 추천한 코드가 처음에 내가 생각했던 방식이지만
# 원래 문자열에 다시 어떻게 넣지? 라는 고민을 하다가 포기했다.
# 조금만 더 생각을 다듬으면 점점 괜찮아질 듯

import sys

input=sys.stdin.readline

s=input().strip()

letters = [i for i in s if i.isalpha()]
letters.reverse()

result=[]

idx=0
for c in s:
  if c.isalpha():
    result.append(letters[idx])
    idx+=1
  else:
    result.append(c)
print("".join(result))


# import sys

# input=sys.stdin.readline

# str=input().strip()

# stack=[]
# for i in range(len(str)):
#   stack.append([i,str[i]])

# lt=0
# rt=len(stack)-1
# while(lt<rt):
#   if(('a'<=stack[lt][1]<='z' or 'A'<=stack[lt][1]<='Z')
#      and
#      ('a'<=stack[rt][1]<='z' or 'A'<=stack[rt][1]<='Z')):
#     tmp=stack[lt][1]
#     stack[lt][1]=stack[rt][1]
#     stack[rt][1]=tmp
#     lt+=1
#     rt-=1
#   elif(('a'<=stack[lt][1]<='z' or 'A'<=stack[lt][1]<='Z')
#        and
#        not ('a'<=stack[rt][1]<='z' or 'A'<=stack[rt][1]<='Z')):
#     rt-=1
#   elif(not ('a'<=stack[lt][1]<='z' or 'A'<=stack[lt][1]<='Z')
#        and
#        ('a'<=stack[rt][1]<='z' or 'A'<=stack[rt][1]<='Z')):
#     lt+=1
#   else:
#     lt+=1
#     rt-=1
# for i in range(len(stack)):
#   print(stack[i][1],end="")