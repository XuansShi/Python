# 示例10-20：从pdf文件中提取数据
import pdfplumber

# 打开pdf文件
with pdfplumber.open('第2章：MATLAB入门知识.pdf') as pdf:# 文件类型的后缀不要忘了
    for i in pdf.pages:
        print(i.extract_text()) # 使用extract_text方法提取内容
        print(f'----------第{i.page_number}页结束----------')













