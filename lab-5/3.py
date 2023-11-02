from random import randint
n = [randint(-100, 100) for i in range(randint(0, 10**6))]
dp = len(n)*[1]

for i in range(1, len(n)):
    if n[i - 1] < n[i]:
        dp[i] = dp[i - 1] + 1

print(max(dp), n[dp.index(max(dp)) - max(dp) + 1: dp.index(max(dp)) + 1])
