import random
import time

while True:
    s = random.randint(1, 3)
    time.sleep(s)
    print("皮蛋可爱哒 "*2)
    if s < 2:
        print("老婆可爱哒")
        continue
    else:
        print("大王可爱哒")
