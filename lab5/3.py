from random import randint
n = [randint(-100, 100) for i in range(10)]
dp = len(n)*[1]

for i in range(1, len(n)):
    if n[i - 1] < n[i]:
        dp[i] = dp[i - 1] + 1

print('Входные данные', *n)
print('Длинна последовательности', max(dp))
print('Последовательность', *n[dp.index(max(dp)) - max(dp) + 1: dp.index(max(dp)) + 1])
