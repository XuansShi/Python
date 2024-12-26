#需要使用到open函数
fp= open('note.txt','w')#先创建一个文件    'w'可写write
print("北京欢迎你",file = fp) #将“北京欢迎你”输出到note.txt文件中
fp.close()#关闭文件






















