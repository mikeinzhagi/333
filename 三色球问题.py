print("red yellow green")
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t'*2, green)
#
# 以下是错误的思路
# import random
# balls = ['red', 'red', 'red', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green']
# # print(len(balls))
# for item in range(20):
#     pick = []
#     for i in range(8):
#         pick.append(random.choice(balls))
#     red = pick.count('red')
#     yellow = pick.count('yellow')
#     green = pick.count('green')
#     list = [red, yellow, green]
#     print(list)