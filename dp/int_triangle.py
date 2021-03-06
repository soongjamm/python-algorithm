# 정수 삼각형
# http://acmicpc.net/problem/1932

n = int(input())
data = []
dp = []
for _ in range(n):
  l = list(map(int, input().split()))
  data.append(l)
  dp.append(l)

res = 0
for i in range(1, n):
  for j in range(i+1):
    if j==0:
      left = 0
    else:
      left = dp[i-1][j-1]
    if j==i:
      right = 0
    else:
      right = dp[i-1][j]
    dp[i][j] = dp[i][j] + max(left, right)
    res = max(res, dp[i][j])

print(res)
  