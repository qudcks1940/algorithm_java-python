# import sys
# input=sys.stdin.readline

# str=input().strip().split()

# answer=[]

# for i in range(0,len(str[0])):
#   left=i
#   right=i
#   while left>=0 or right<len(str[0]):
#     # str[0][left]==str[1] or str[0][right]==str[1]
#     if str[0][i]==str[1]:
#       answer.append(0)
#       break
#     elif left>=0 and str[0][left]==str[1]:
#       answer.append(abs(i-left))
#       break
#     elif right<len(str[0]) and str[0][right]==str[1]:
#       answer.append(abs(i-right))
#       break
#     else:
#       left-=1
#       right+=1
# for j in answer:
#   print(j,end=" ")


# GPT 코드
# 매우 깔끔
# import sys
# input = sys.stdin.readline

# s, target = input().strip().split()

# answer = []
# n = len(s)

# for i in range(n):
#     # 현재 위치의 문자가 타겟이면 거리 0
#     if s[i] == target:
#         answer.append(0)
#         continue

#     # 양쪽으로 확장하며 타겟 문자를 찾기
#     left = i - 1
#     right = i + 1
#     while left >= 0 or right < n:
#         if left >= 0 and s[left] == target:
#             answer.append(i - left)
#             break
#         if right < n and s[right] == target:
#             answer.append(right - i)
#             break
#         left -= 1
#         right += 1

# print(' '.join(map(str, answer)))


# GPT가 짜준 시간 복잡도, 공간 복잡도 모두 O(n)인 코드드
import sys
input = sys.stdin.readline

s, target = input().strip().split()
n = len(s)
answer = [0] * n

# 왼쪽에서 오른쪽으로 탐색: 현재까지의 타겟 등장 위치와의 거리 계산
prev = -10**9  # 매우 작은 초기값 (음의 무한대처럼)
for i in range(n):
    if s[i] == target:
        prev = i
    answer[i] = i - prev

prev = 10**9
for i in range(n-1,-1,-1):
    if s[i] == target:
        prev = i

    answer[i] = min(prev - i,answer[i])

print(' '.join(map(str,answer)))