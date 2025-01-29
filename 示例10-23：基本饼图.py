# 示例10-23：基本饼图
# 1 导入pyecharts包
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 2 找到相应图形模板
'''
这个是官方示例：
c = (
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_base.html")
)
    # 上面这个示例中最核心的是这个列表 [list(z) for z in zip(Faker.choose(), Faker.values())]
    
    
# 
'''

# 3 准备数据
lst = [['哈士奇', 150], ['萨摩耶', 112], ['泰迪', 32], ['金毛', 96], ['牧羊犬', 111], ['吉娃娃', 69], ['柯基', 75]]
c = (
    Pie()
    .add("", lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="示例10-23：基本饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("dogs.html")
)

# 4 个性化修饰
    # 直接在帮助文档里https://gallery.pyecharts.org/#/README找到喜欢的样式，然后改数据就行了



