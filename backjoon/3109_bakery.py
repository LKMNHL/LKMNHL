def dfs():
    global cnt
    delta=[[-1, 1], [0, 1], [1, 1]] # 상우, 우, 하우 (최대한 위쪽으로 붙어야 많은 파이프를 배치할 수 있음)
    while stack:
        # print(visited)
        i, j=stack.pop()

        if j==M-1: # 종료조건
            cnt+=1 # 갈 수 있는 길 계수
            return

        for di, dj in delta: # delta 방향으로 탐색
            ni, nj=i+di, j+dj

            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]: # 유효 인덱스, 방문하지 않은 곳이면
                if arr[ni][nj]=='.': # 통로일 때
                    stack.append([ni, nj])
                    visited[ni][nj]=1
                    break

'''
5 5
.xx..
..x..
.....
...x.
...x.

'''

N, M=list(map(int, input().split()))
arr=[list(input().strip()) for _ in range(N)]

stack=[]
visited=[[0]*M for _ in range(N)]

cnt=0


for i in range(N):
    if arr[i][1]=='.' and not visited[i][1]:
        stack.append([i, 1])
        visited[i][1]=1
        dfs()

print(cnt)