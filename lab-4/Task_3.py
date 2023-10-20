n = 15
matr = [[int(i) for i in input().split()] for _ in range(n)]

used = []
for _ in range(n):
    pp = []
    for _ in range(n):
        pp.append(False)
    used.append(pp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = [-1, -1, []]


def dfs(iv, jv, path):
    if matr[iv][jv] == 0:
        if jv == n-1 or iv == n-1 or jv == 0:
            ans[0] = iv
            ans[1] = jv
            ans[2] = path

    if used[iv][jv]:
        return [-1, -1]

    used[iv][jv] = True

    for i in range(4):
        niv = iv + dx[i]
        njv = jv + dy[i]
        if (niv >= 0) and (niv < n) and (njv >= 0) and (njv < n):
            if matr[niv][njv] == 0:
                if not used[niv][njv]:
                    dfs(niv, njv, path + [(niv, njv)])
    used[iv][jv] = False



l = 1
for i in range(1, n):
    if matr[i][0] == 0:
        dfs(i, 0, [(i, 0)])
        if ans != [-1, -1]:
            break

if ans[0] == -1 and ans[1] == -1:
    print("В лабиринте нет выхода")
else:
    print(f'Выход из лабиринта находится на {ans[0]+1} строке в {ans[1]+1} столбце')
    for i in range(n):
        for j in range(n):
            if matr[i][j] == 1:
                if (i == 0 or i == n-1) and (j != 0 and j != n-1):
                    matr[i][j] = "-"
                elif (i != 0 and i != n - 1) and (j == 0 or j == n - 1):
                    matr[i][j] = "|"
                elif (i == 0 and j == 0) or (i == n-1 and j == 0) or (i == n-1 and j == n-1) or (i == 0 and j == n-1):
                    matr[i][j] = "+"
                else:
                    matr[i][j] = "#"
            else:
                matr[i][j] = "O"
    for tp in ans[2]:
        matr[tp[0]][tp[1]] = "X"


    for i in range(n):
        print(*matr[i])
'''
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 1 0 1 0 0 0 0 1 0 1
1 0 1 1 1 1 0 1 0 1 1 0 1 0 1
1 0 1 0 0 0 0 1 0 1 1 0 1 0 1
1 0 1 1 1 1 0 1 0 0 1 0 1 0 1
1 0 0 0 0 1 0 1 0 1 1 0 1 0 1
1 0 1 1 1 1 0 1 0 1 1 0 1 0 1
0 0 1 1 0 1 0 1 0 1 0 0 1 0 1
1 0 1 0 0 0 0 0 0 1 1 0 1 0 1
1 0 1 1 1 0 1 1 0 0 1 0 1 0 0
1 0 0 1 1 0 1 1 1 1 1 0 1 0 1
1 1 0 0 0 0 1 0 0 0 0 0 1 0 1
1 0 0 1 1 1 1 1 1 1 1 0 1 0 1
1 1 1 1 0 0 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
'''
