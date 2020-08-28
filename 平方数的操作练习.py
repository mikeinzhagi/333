# import math
# num = 0
# while True:
#     num += 1
#     if isinstance(math.sqrt((num + 100)), int):
#         if isinstance(math.sqrt((num + 268)), int):
#             print(num)
#             break


import math
for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if x * x == i + 100 and y * y == i + 268:
        print(i)