# 5648. [모의 SW 역량테스트] 원자 소멸 시뮬레이션

def solution(arr):
    ans=0

    # 직교 좌표계 기준
    # n.5 위치에서 만나는 경우를 고려하여, 0.5 단위로 이동
    delta = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

    while len(arr)>=2:
        for i in range(len(arr)):
            arr[i][0]+=delta[arr[i][2]][0] # x(열) 이동
            arr[i][1]+=delta[arr[i][2]][1] # y(행) 이동

        location={} # 현재 원자의 위치를 딕셔너리로
        # 딕셔너리 메서드로 구현가능할듯...
        for atom in arr:
            try:
                location[(atom[0], atom[1])].append(atom) # 해당 위치 좌표:원자들로 저장
            except Exception:
                location[(atom[0], atom[1])]=[atom] # 최초 발생이라면 초기화

        arr=[]
        for l in location:
            if len(location[l])>=2: # 원자 충돌
                for ats in location[l]:
                    ans+=ats[3] # 에너지 더하기
            else:
                if -1000<=location[l][0][0]<=1000 and -1000<=location[l][0][1]<=1000:
                    arr.append(location[l][0])
    return ans

'''
2
4
-1000 0 3 5
1000 0 2 3
0 1000 1 7
0 -1000 0 9
4
-1 1 3 3
0 1 1 1
0 0 2 2
-1 0 0 9

'''


T=int(input().strip())
for tc in range(1, T+1):
    N=int(input().strip()) # 원자 수
    arr=[list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {solution(arr)}')