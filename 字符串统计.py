# count('I love fishc.com','I love you , you love me')
#
# def count(s):
#     s1 = s[1]
#     s2 = s[2]
# print(s1)
# print(s2)


# def count(*param):
#     length = len(*param)
#     for i in range(length):
#         letters = 0
#         space = 0
#         digit = 0
#         others = 0
#         for each in list(param):
#             if each.isalpha():
#                 letters += 1
#             elif each.isdigit():
#                 digit += 1
#             elif each == "":
#                 space += 1
#             else:
#                 others += 1
#     print('第%d个字符共有,英文字符%d,数字%d个,空格%d个,其他%d个.' %(i+1, letters, digit, space, others))
#
# count('I love fish.com')


def count(*params):
    '编写一个函数，分别统计出传入字符串参数的英文字符、空格、数字和其它字符的个数'
    param_count = 0
    for each in params:
        param_count += 1
        letters = spaces = digits = others = 0
        for item in list(each):
            if str.isdigit(item):
                digits += 1
            elif str.isspace(item):
                spaces += 1
            elif str.isalpha(item):
                letters += 1
            else:
                others += 1
        print(('第%d个参数中有%d个英文字符，%d个空格，%d个数字，其它的%d个') % (param_count, letters, spaces, digits, others))


count('hello world 123!', 'public static void main')