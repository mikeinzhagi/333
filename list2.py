member = ['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '恬静', '福禄娃娃', '竹林小溪', 'Crazy迷恋']
# member[0], member[1] = member[1], member[0]
member.remove('恬静')
del member[1]

member.pop()
print(member)
