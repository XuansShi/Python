# 示例10-18：将爬取的景区天气数据存储到Excel
import weather
import openpyxl

html = weather.get_html() # 发送请求，返回响应结果
lst = weather.parse_html(html) # 解析数据

# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook()

# 确认数据格式正确
print(lst)

# 在Excel文件中创建工作表
worksheet = workbook.create_sheet("景区天气")# 工作表的名称是 景区天气

# 向工作表中添加数据
for item in lst:
    worksheet.append(item)

# 保存工作簿
workbook.save("景区天气.xlsx")





















