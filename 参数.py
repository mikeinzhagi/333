def test(*parameters):
    print('参数的长度是', len(parameters))
    print('第二个参数是', parameters[4])


test(23, 32, 345, 'dawang', '代发费', 34)