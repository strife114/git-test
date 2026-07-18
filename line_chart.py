import random
from pyecharts.charts import Line
from pyecharts import options as opts

# 随机生成数据
x_data = [f"第{i}天" for i in range(1, 31)]
y_data = [round(random.uniform(10, 100), 2) for _ in range(30)]

# 创建折线图
line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "随机数据",
        y_data,
        is_smooth=True,                          # 平滑曲线
        symbol="circle",
        symbol_size=6,
        linestyle_opts=opts.LineStyleOpts(width=2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="随机数据折线图", subtitle="30天趋势"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        xaxis_opts=opts.AxisOpts(name="时间"),
        yaxis_opts=opts.AxisOpts(name="数值"),
    )
)

# 输出 HTML 文件
output_path = "E:/New_AI/pyproj/line_chart.html"
line.render(output_path)
print(f"折线图已生成：{output_path}")
