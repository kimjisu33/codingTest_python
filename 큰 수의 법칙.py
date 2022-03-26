
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

#데이터 정렬
data.sort()
first=data[n-1] #가장 큰 수
second=data[n-2] #두번째로 큰 수

sum=0

while True:
    for i in range(k) :
        if m==0:
            break
        sum+=first
        m-=1
    if m==0:
        break
    sum+=second
    m-=1

print(sum)
