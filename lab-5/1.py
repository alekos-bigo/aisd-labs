def maximize_stolen_value(N, M, K, weights, values):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i - 1][j]
            if weights[i - 1] <= K:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + values[i - 1])

    return dp[N][M]


N = 4
M = 2
K = 3
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]

max_stolen_value = maximize_stolen_value(N, M, K, weights, values)
print("Максимальная сумма украденных экспонатов:", max_stolen_value)
