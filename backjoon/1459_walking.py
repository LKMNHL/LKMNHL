def solution(i, j, cost):
    print(i, j)
    global min_cost
    if i==Y and j==X:
        if min_cost>cost:
            min_cost=cost
            return

    delta=[[-1, 0], [0, 1], [1, 1]] # 하, 우, 우하
    # 대각선 하나=아래+오른쪽

    for i in range(3):
        ni, nj=i+delta[i][0], j+delta[i][1]

        if ni<0 or ni>=Y or nj<0 or nj>=X:
            continue

        if i<2:
            cost+=W
        else:
            cost+=S

        solution(ni, nj, cost)


# X: 집 열 Y: 집 행, W: 한 블록 걷는 데 걸리는 시간, S: 대각선으로 블록을 가로지르는 시간
X, Y, W, S=list(map(int, input().split()))
min_cost=10000000000000000000000
solution(0, 0, 0)
print(min_cost)