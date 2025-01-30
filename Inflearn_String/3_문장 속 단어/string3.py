import sys

input=sys.stdin.readline().strip

sentence=input().split()

max=0
answer=""
for i in sentence:
  if len(i)>max:
    max=len(i)
    answer=i

# # GPT 코드
# max_len = 0
# answer=""
# for word in input().split():
#     if (len(word)) > max_len:
#         max_len = len(word)
#         answer = word

print(answer)
