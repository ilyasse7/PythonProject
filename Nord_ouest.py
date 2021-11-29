def nord_ouest(t,l):
    for i in range(len(t[3])):
        for j in range(len(t[4])):
            if t[3][i] >= t[4][j]:
                l[i][j] = t[4][j]
                t[3][i] = t[3][i] - t[4][j]
                t[4][j] = 0
            else:
                l[i][j] = t[3][i]
                t[4][j] = t[4][j] - t[3][i]
                t[3][i] = 0

    return l



