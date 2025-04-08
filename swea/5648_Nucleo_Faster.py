OFFSET=2000 # 정수 좌표에서 만나도록... 1000*2
MAX=4001 # 정수 좌표에서 만나도록... -1000~1000 범위이니까 2000*2+1

# 이 부분이 포인트
def hashing(x, y):
    return x*MAX+y

def unhasing(value):
    x=value//MAX
    y=value%MAX
    return x, y

def solution (arr):
    di=[1, -1, 0, 0]
    dj=[0, 0, -1, 1]

    ans=0

    n=N
    while n>0:
        next_atoms={} # 다음 위치 모음
        deleted=set() # 충돌 위치
        mini_energy=0

        for key, (direction, energy) in arr.items():
            i, j=unhasing(key) # 언해싱으로 실제 좌표 추출
            ni, nj=i+di[direction], j+dj[direction]
            hashed=hashing(ni, nj)

            # 유효 좌표 검사 (문제 조건에 의해...)
            if ni<0 or ni>4000 or nj<0 or nj>4000:
                n-=1 # 사용 가능 원자 개수 감소
                continue

            if hashed in next_atoms: # 다음 위치가 이미 정의되었다면 == 충돌
                deleted.add(hashed) # 삭제 원소에 넣기
                n-=1 # 원소 개수 감소
                mini_energy+=energy # 에너지 증가
            else: # 처음 가는 위치면 정의
                next_atoms[hashed]=(direction, energy)

        arr.clear() # 이동이 끝난 원자 위치 초기화
        for key, (direction, energy) in next_atoms.items(): # 다음 위치 정의된 것 검사
            if key in deleted: # 충돌이 일어난 경우, (이전에서는 이후에 도착하여 충돌한 원자만 뺐으므로 최초의 것을 빼줘야 함)
                n-=1
                mini_energy+=energy
            else:
                arr[key]=(direction, energy)
        ans+=mini_energy

    return ans

T=int(input().strip())
for tc in range(1, T+1):
    N=int(input().strip()) # 원자 수

    arr={}
    for _ in range(N):
        a, b, c, d=map(int, input().split())
        x=b*2+OFFSET # 직교 좌표계를 행렬 형식으로 바꾸기 위해 y를 x(행)으로
        y=a*2+OFFSET
        arr[hashing(x, y)]=(c, d) # 좌표:(방향, 에너지) 형태로 저장

    print(f'#{tc} {solution(arr)}')