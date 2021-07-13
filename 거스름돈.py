money = 1260 #input("거스름돈을 입력하세요 --> ")
cnt = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    cnt += money//coin
    money %= coin

print("동전 개수 : ",cnt)
