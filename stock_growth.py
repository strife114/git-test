# 定义变量
name = "传智播客"                          # 公司名
stock_price = 19.99                        # 当前股价
stock_code = "003032"                      # 股票代码
stock_price_daily_growth_factor = 1.2      # 股票每日增长系数（浮点数）
growth_days = 7                            # 增长天数

# 计算：经过 growth_days 天的增长后，股价达到了多少
final_price = stock_price * (stock_price_daily_growth_factor ** growth_days)

# 第一行：使用 f-string 方式输出
print(f"公司：{name}, 股票代码：{stock_code}, 当前股价：{stock_price}")

# 第二行：使用 % 占位符方式输出（浮点数保留 2 位小数）
print("每日增长系数是：%.2f  经过%d天的增长后，股价达到了：%.2f" %
      (stock_price_daily_growth_factor, growth_days, final_price))
