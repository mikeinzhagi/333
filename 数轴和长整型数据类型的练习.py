profit = int(input("请输入您的净利润："))
arr = [1000000,600000,400000,200000,100000,0]
Money_rate = [0.01,0.015,0.03,0.05,0.075,0.1]
bonus = 0
for i in range(0,6):
    if profit > arr[i]:    #判断净利润的范围
        bonus += (profit-arr[i])*Money_rate[i]   #奖金的计算
        print((profit-arr[i])*Money_rate[i])
        profit = arr[i]   #重新复制净利润，进行低阶段判断
print(bonus)