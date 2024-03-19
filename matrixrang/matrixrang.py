m = [[4, 4, 4],
     [4, 4, 4],
     [4, 4, 4]]


def f(m, k):
    for i in range(k + 1, len(m)):
        if m[i][k] != 0:
            for j in range(k, len(m[i])):
                if j == k:
                    c = m[k][k] / m[i][j]
                m[i][j] = m[i][j] * c - m[k][j]
    return m


def p(m):
    n_m = []
    for i in m:
        if i != [0] * len(m[0]):
            n_m.append(i)
    return sorted(n_m, reverse=True)


m = p(m)

for k in range(len(m)):
    m = f(m, k)
    m = p(m)

print(len(m))
