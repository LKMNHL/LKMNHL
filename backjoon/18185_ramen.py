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

    for i in range(N-2):
        if arr[i+1]>arr[i+2]:
            times=min(arr[i], arr[i+1]-arr[i+2])
            arr[i]-=times
            arr[i+1]-=times
            ans+=5*times

            


N=int(input())
arr=list(map(int, input().split()))
print(solution(N, arr))