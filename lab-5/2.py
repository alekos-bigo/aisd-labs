def mo(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1

            m[i][j] = int(1e9 + 7)

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n-1]


n = int(input('Введите количество матриц:\n'))
print("Введите размеры матриц:")
matr = [[int(i) for i in input().split()] for _ in range(n)]
df = []
for i in matr:
    df.append(i[0])
df.append(matr[-1][1])
ans = mo(df)
print(f'Минимальное число операций {ans}')
