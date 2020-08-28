num=0
for i in range(1, 5):

    for j in range(1, 5):

        for k in range(1, 5):

            if (i != k) and (i != j) and (j != k):
                num+=1
                print(num,i*100+j*10+k)