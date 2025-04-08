# 5658. [모의 SW 역량테스트] 보물상자 비밀번호

# N//4 씩 커트
def solution(arr):
    cnt=N//4

    nums=[]
    for h in range(cnt):
        for i in range(0, N, cnt):
            number = ''
            for j in range(cnt):
                number+=arr[i+j]
            # print(number)
            if number not in nums:
                nums.append(number)
        end_ptr=arr.pop()
        arr=[end_ptr]+arr

    nums.sort(reverse=True)
    # print(nums)
    return nums[K-1]

'''
5
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8

'''

T=int(input().strip())
for tc in range(1, T+1):
    N, K=map(int, input().split()) # 숫자 개수, 크기 순서
    arr=list(input().strip()) # len(arr)=N

    hex=solution(arr)
    ans=int(hex, 16)
    print(f'#{tc} {ans}')