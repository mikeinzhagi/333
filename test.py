import random
answer = random.randint(1, 10)
gugu = 3
while gugu > 0:
    temp = input("请输入一个数字：")
    guess = int(temp)
    gugu = gugu - 1
    if guess == answer:
        print("你是小甲鱼心里的蛔虫！")
        print("哼，猜中了也没奖励")
        break
    else:
        if guess < answer:
            print("小啦！")
        else:
            print("大啦！")
print("游戏结束")
