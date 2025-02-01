# 示例10-19：从Excel文件中读取数据
import openpyxl
# 打开工作簿
workbook = openpyxl.load_workbook('景区天气.xlsx')

# 选择要操作的工作表
sheet = workbook['景区天气']

# 表格数据是二维列表，先遍历行，再遍历列
lst = []  # 存储行数据
for row in sheet.rows:  # 直接迭代sheet.rows，而不是sheet.rows()
    sublst = []  # 存储单元格数据
    for cell in row:  # 遍历cell单元格
        sublst.append(cell.value)
    lst.append(sublst)


# 打印
for item in lst: print(item)










