def maximize_stolen_value(N, M, K, weights, values):
    dp = [[0] * (K * M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K * M + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    max_value = dp[N][K * M]
    stolen_items = []
    j = K * M

    for i in range(N, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            stolen_items.append(i - 1)
            j -= weights[i - 1]

    return max_value, stolen_items[::-1]


N = 4
M = 2
K = 3
weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]

max_value, stolen_items = maximize_stolen_value(N, M, K, weights, values)
print("Максимальная стоимость украденных экспонатов:", max_value)
print("Экспонаты, которые вор унес:", *stolen_items)
