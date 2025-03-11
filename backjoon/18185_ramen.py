def time_over(N, arr):
    ans=0

    while sum(arr)>0:
        start = 0
        buy = [0] * 3

        for i in range(N):
            if arr[i]:
                start+=1
                arr[i]-=1
            else:
                if start==1:
                    buy[0]+=1
                elif start==2:
                    buy[1]+=1
                elif start==3:
                    buy[2]+=1
                start=0

        if start == 1:
            buy[0] += 1
        elif start == 2:
            buy[1] += 1
        elif start == 3:
            buy[2] += 1

        # print(buy)

        ans+=buy[0]*3
        ans+=buy[1]*5
        ans+=buy[2]*7

    return ans

def solution(N, arr):
    ans=0
    # 1개만 구매: 개 당 3원으로 가장 비쌈
    # 2개 구매: 개 당 2.5원
    # 3개 구매: 개 당 1원
    # 처음부터 3개를 구매할 경우, 자신+1>자신+2일 때 최적이 아님
    # 자신, 자신+1 먼저 소진하는 방식으로...
    for i in range(len(arr)-2):
        if arr[i+1]>arr[i+2]: # 나+1이 나+2보다 큰 경우 (2묶음 -> 3묶음 -> 1묶음 순)
            times=min(arr[i], arr[i+1]-arr[i+2])
            arr[i]-=times
            arr[i+1]-=times
            ans+=5*times

            remain_times=min(arr[i], arr[i+1], arr[i+2])
            arr[i]-=remain_times
            arr[i+1]-=remain_times
            arr[i+2]-=remain_times
            ans+=7*remain_times

            ans += arr[i] * 3

        else: # 나+2가 나+1보다 큰 경우 (3묶음 -> 2묶음 -> 1묶음 순)
            times=min(arr[i], arr[i+1], arr[i+2])
            arr[i]-=times
            arr[i+1]-=times
            arr[i+2]-=times
            ans+=7*times

            remain_times=min(arr[i], arr[i+1])
            arr[i]-=remain_times
            arr[i+1]-=remain_times
            ans+=5*remain_times

            ans += arr[i] * 3

    return ans

N=int(input())
arr=list(map(int, input().split()))+[0, 0]
print(solution(N, arr))