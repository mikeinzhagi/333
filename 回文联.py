# s = input('请输入一句话')
# s = str(s)
# l = len(s)
# for i in range(l):
#     if s[i] != s[l-1-i]:
#         flag = 1
#     else:
#         print('是回文联')
# if flag == 1:
#     print('不是回文联')

def huiwen(s):
    list1 = list(s)
    list2 = list1[::-1]  # []使用列表  颠倒使用::-1
    print(list1)
    print(list2)
    if list1 == list2:
        return '是回文联'
    else:
        return '不是回文联'


print(huiwen('上海自来水来自海上'))
