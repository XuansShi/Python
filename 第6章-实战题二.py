#第6章-实战题二 统计指定字符出现的次数
s='HelloPython,HelloJava,hellophp'
word=input('请输入要统计的字符:')
print('{0}在{1}一共出现了{2}'.format(word,s,s.upper().count(word)))