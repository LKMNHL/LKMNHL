def dfs():
    global cnt
    delta=[[0, 1], [-1, 1], [1, 1]] # 상, 상우, 하우
    while stack:
        i, j=stack.pop()

        if j==M-2: # 종료조건
            cnt+=1 # 갈 수 있는 길 계수
            return

        if visited[i][j]: # 방문했으면 탐색 중지
            continue

        for di, dj in delta: # delta 방향으로 탐색
            ni, nj=i+di, j+dj

            if 0<=ni<N and 0<=nj<M: # 유효범위일 때
                if arr[ni][nj]=='.': # 통로일 때
                    stack.append([ni, nj])
                    visited[ni][nj]=1







N, M=list(map(int, input().split()))
arr=[list(input().split()) for _ in range(N)]

stack=[]
visited=[[0]*M for _ in range(N)]

cnt=0

for i in range(N):
    for j in range(1, M-1):
        if arr[i][j]=='.' and not visited[i][j]:
            stack.append([i, j])
            visited[i][j]+=1
            dfs()
