# -*- coding:utf-8 -*
from pyecharts import Map


# attr, value要显示的数值
value = [20, 100]
attr = ['余杭区', '萧山区']
m = Map('杭州地图示例图', width=600, height=400)

# add() 用于添加图表的数据和设置各种配置项
# visual_range=[10000, 300000]  指定坐标范围
# is_label_show=True  显示每个点的值x
m.add('', attr, value, maptype=u'杭州', visual_range=[0, 100], is_label_show=True, is_visualmap=True, visual_text_color='#000')

# show_config() 打印输出图表的所有配置项
m.show_config()

# render() 生成 .html 文件
m.render()
