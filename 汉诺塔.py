def hanoi(n, x, y, z):
    if n == 1:
        print(x,' --> ', z)
    else:
        hanoi(n-1, x, z, y)
        # 将前n-1个盘子从x移动到y上
        print(x, ' --> ', z)
        # 将y上n-1个盘子移动到z上
        hanoi(n-1, y, x, z)

print(hanoi(4,'左','中','右'))

