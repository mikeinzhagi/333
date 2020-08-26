i = 0
n = 0
list = []
while True:
    i += 1
    if i % 2 == 1:
        if i % 3 == 2:
            if i % 5 == 4:
                if i % 6 == 5:
                    if i % 7 == 0:
                        print(i, end=' \n')
                        n += 1
                        list.append(i)
                        if n >= 10:
                            print(list)
                            break