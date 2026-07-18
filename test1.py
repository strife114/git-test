# -*- coding: utf-8 -*-
"""
============================================================
  Python 入门教程 —— 从零开始学 Python
  作者: 新手学习笔记
  日期: 2026-07-08
============================================================

这个文件适合完全没有编程基础的初学者。
每一部分都有详细的注释和示例，建议按顺序阅读和运行。
你可以一段一段地运行代码来观察输出结果。

如何运行：
  在终端中输入: python test1.py
  或者在 IDE (如 PyCharm / VS Code) 中直接点击运行按钮。
"""

# ============================================================
#  第 1 课：你的第一行代码 —— 输出 Hello World
# ============================================================

# print() 是 Python 最常用的函数，用来把内容显示在屏幕上
print("hello world")  # 这是你写的第一行代码！

# 字符串可以用 双引号 " 或 单引号 ' 括起来
print('hello world')  # 效果完全一样

# 让我们多试试！
print("=" * 50)  # 打印一条分隔线（字符串 * 数字 = 重复）
print("欢迎来到 Python 的世界！")
print("=" * 50)
print()  # 空行 —— 什么都不输出，只是换行


# ============================================================
#  第 2 课：变量 —— 给数据起个名字
# ============================================================

# 变量就像一个 "贴了标签的盒子"，你可以把东西放进去
# Python 中不需要声明类型，直接赋值即可

name = "小明"         # 字符串 (str)  —— 文字
age = 18              # 整数 (int)    —— 整数
height = 1.75         # 浮点数 (float) —— 小数
is_student = True     # 布尔值 (bool)  —— 真/假

print("我叫", name)
print("我今年", age, "岁")
print("我的身高是", height, "米")
print("我是学生吗？", is_student)
print()

# Python 3.6+ 支持 f-string，更直观地拼接变量和文字
print(f"大家好，我叫{name}，今年{age}岁，身高{height}米。")
print()


# ============================================================
#  第 3 课：基本数据类型
# ============================================================

print("=" * 50)
print("第 3 课：基本数据类型")
print("=" * 50)

# --- 3.1 字符串 (str) ---
# 字符串就是一段文字
greeting = "Hello"
target = "Python"

# 字符串拼接
full_greeting = greeting + ", " + target + "!"  # 用 + 号拼接
print(full_greeting)  # 输出: Hello, Python!

# 字符串方法（字符串自带的功能）
print(greeting.upper())       # 转大写: HELLO
print(greeting.lower())       # 转小写: hello
print(len(greeting))          # 长度: 5
print(greeting[0])            # 取第1个字符: H (索引从0开始!)
print(greeting[-1])           # 取最后一个字符: o
print(greeting[1:4])          # 切片，取第2到第4个字符: ell

# f-string 格式化
pi = 3.1415926
print(f"π 保留两位小数: {pi:.2f}")   # 3.14
print(f"π 保留四位小数: {pi:.4f}")   # 3.1416
print()

# --- 3.2 数字 (int / float) ---
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"加法 a + b = {a + b}")      # 13
print(f"减法 a - b = {a - b}")      # 7
print(f"乘法 a * b = {a * b}")      # 30
print(f"除法 a / b = {a / b}")      # 3.333...（总是返回浮点数）
print(f"整除 a // b = {a // b}")    # 3（只取整数部分）
print(f"取余 a % b = {a % b}")      # 1（除完剩下的）
print(f"乘方 a ** b = {a ** b}")    # 1000（10的3次方）
print()

# --- 3.3 布尔值 (bool) ---
# 只有 True 和 False 两个值
print(f"5 > 3: {5 > 3}")         # True
print(f"5 < 3: {5 < 3}")         # False
print(f"5 == 5: {5 == 5}")       # True（== 判断是否相等）
print(f"5 != 3: {5 != 3}")       # True（!= 判断是否不相等）
print()

# --- 3.4 类型检查和转换 ---
print(f"name 的类型是: {type(name)}")        # <class 'str'>
print(f"age 的类型是: {type(age)}")           # <class 'int'>

# 类型转换
number_str = "123"
number_int = int(number_str)       # 字符串 → 整数
print(f"转换后: {number_int}，类型: {type(number_int)}")

pi_str = str(3.14)                 # 小数 → 字符串
print(f"转换后: {pi_str}，类型: {type(pi_str)}")
print()


# ============================================================
#  第 4 课：列表 —— 一组有序的数据
# ============================================================

print("=" * 50)
print("第 4 课：列表 (list)")
print("=" * 50)

# 列表用方括号 []，可以装任何东西
fruits = ["苹果", "香蕉", "橘子", "葡萄", "西瓜"]
print(f"水果列表: {fruits}")

# 访问元素（索引从 0 开始！）
print(f"第1个水果: {fruits[0]}")     # 苹果
print(f"第3个水果: {fruits[2]}")     # 橘子
print(f"最后一个水果: {fruits[-1]}")  # 西瓜（负数从末尾数）

# 切片
print(f"前3个水果: {fruits[0:3]}")   # ['苹果', '香蕉', '橘子']
print(f"后2个水果: {fruits[-2:]}")   # ['葡萄', '西瓜']

# 列表操作
fruits.append("草莓")               # 在末尾添加
print(f"添加后: {fruits}")

fruits.remove("香蕉")               # 删除指定元素
print(f"删除香蕉后: {fruits}")

fruits.insert(1, "芒果")            # 在指定位置插入
print(f"在第2个位置插入芒果: {fruits}")

print(f"列表长度: {len(fruits)}")   # 有几个元素
print(f"橘子在第{fruits.index('橘子') + 1}个位置")  # 查找位置
print()

# 列表可以装各种类型
mixed_list = [42, "hello", 3.14, True, [1, 2, 3]]  # 甚至能装另一个列表！
print(f"混合列表: {mixed_list}")
print()


# ============================================================
#  第 5 课：字典 —— 键值对的数据
# ============================================================

print("=" * 50)
print("第 5 课：字典 (dict)")
print("=" * 50)

# 字典用花括号 {}，是 "键: 值" 的集合
# 就像一本真正的字典：查 "苹果" → 找到 "apple"

student = {
    "姓名": "小明",
    "年龄": 18,
    "班级": "高一(3)班",
    "成绩": {
        "语文": 85,
        "数学": 92,
        "英语": 78
    }
}

print(f"学生信息: {student}")
print(f"姓名: {student['姓名']}")           # 用键来取值
print(f"数学成绩: {student['成绩']['数学']}")  # 嵌套取值

# 添加/修改
student["性别"] = "男"      # 新增
student["年龄"] = 19        # 修改
print(f"更新后: {student}")

# 获取所有键和值
print(f"所有键: {list(student.keys())}")
print(f"所有值: {list(student.values())}")

# 安全取值 —— 用 .get() 避免键不存在时报错
print(f"电话号码: {student.get('电话', '未填写')}")  # 没有就返回默认值
print()


# ============================================================
#  第 6 课：条件判断 —— 让程序做决策
# ============================================================

print("=" * 50)
print("第 6 课：条件判断 (if / elif / else)")
print("=" * 50)

score = 85

# if...elif...else 结构
if score >= 90:
    grade = "A"
    print("太棒了！优秀！")
elif score >= 80:
    grade = "B"
    print("不错，继续保持！")
elif score >= 70:
    grade = "C"
    print("还可以，继续加油！")
elif score >= 60:
    grade = "D"
    print("勉强及格，要加油哦！")
else:
    grade = "F"
    print("不及格，需要更加努力！")

print(f"分数: {score} → 等级: {grade}")
print()

# 多条件组合: and / or / not
temperature = 28
is_sunny = True

if temperature > 25 and is_sunny:
    print("天气又热又晒，记得带防晒！")
elif temperature > 25 and not is_sunny:
    print("虽然热但没太阳，还好还好。")
elif temperature < 10 or not is_sunny:
    print("有点冷或者阴天，多穿点！")
print()


# ============================================================
#  第 7 课：循环 —— 重复执行代码
# ============================================================

print("=" * 50)
print("第 7 课：循环 (for / while)")
print("=" * 50)

# --- 7.1 for 循环 ---
# 遍历列表
print("遍历水果列表:")
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"  * {fruit}")

print()

# range() 函数 —— 生成一系列数字
print("用 range() 数数:")
for i in range(5):          # 0, 1, 2, 3, 4（注意：不包含5！）
    print(f"  第{i}次")

print()
for i in range(1, 6):       # 从1到5
    print(f"  {i}", end=" ")  # end=" " 让输出不换行，用空格分隔
print("\n")

# 枚举 —— 同时获取索引和值
print("编号 水果")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")
print()

# --- 7.2 while 循环 ---
# 只要条件为 True 就一直循环
print("while 循环示例:")
count = 1
while count <= 5:
    print(f"  倒数: {count}")
    count += 1  # count = count + 1 的简写
print()

# --- 7.3 break 和 continue ---
print("break 和 continue:")
for i in range(1, 10):
    if i == 3:
        continue  # 跳过本次循环（跳过3）
    if i == 7:
        break     # 结束整个循环（到7就停）
    print(f"  {i}", end=" ")
print()  # 输出: 1 2 4 5 6
print()


# ============================================================
#  第 8 课：函数 —— 封装可复用的代码块
# ============================================================

print("=" * 50)
print("第 8 课：函数 (def)")
print("=" * 50)


# 定义一个函数
def greet(name):
    """这是一个文档字符串，说明函数的功能"""
    return f"你好，{name}！欢迎学习 Python！"


# 调用函数
print(greet("小明"))
print(greet("小红"))
print()

# 带默认参数的函数
def power(base, exponent=2):
    """计算 base 的 exponent 次方，默认是平方"""
    return base ** exponent


print(f"5的平方: {power(5)}")          # 使用默认值
print(f"5的3次方: {power(5, 3)}")      # 传入参数覆盖默认值
print()

# 多返回值函数
def get_min_max(numbers):
    """返回列表中的最小值和最大值"""
    return min(numbers), max(numbers)  # 用逗号返回多个值


scores = [78, 92, 65, 88, 73]
lowest, highest = get_min_max(scores)  # 多个变量接收
print(f"成绩范围: {lowest} ~ {highest}")
print()

# 不定长参数 *args
def sum_all(*numbers):
    """接受任意多个参数，返回总和"""
    total = 0
    for n in numbers:
        total += n
    return total


print(f"1+2+3 = {sum_all(1, 2, 3)}")
print(f"1+2+3+4+5 = {sum_all(1, 2, 3, 4, 5)}")
print()

# lambda 表达式 —— 一行函数
square = lambda x: x ** 2
print(f"7的平方(lambda): {square(7)}")
print()


# ============================================================
#  第 9 课：用户输入
# ============================================================

print("=" * 50)
print("第 9 课：用户输入 (input)")
print("=" * 50)

# input() 会等待用户输入，返回字符串
# 注意：在脚本中运行时，如果不想每次都输入，
# 可以把下面的 input() 部分注释掉或直接按回车跳过

# user_name = input("请输入你的名字: ")
# print(f"你好，{user_name}！")
# print()

# 模拟输入（不需要真的输入）
print("提示：input() 会等待用户在终端输入内容。")
print("示例：name = input('请输入你的名字: ')")
print()


# ============================================================
#  第 10 课：文件操作
# ============================================================

print("=" * 50)
print("第 10 课：文件操作")
print("=" * 50)

# 写文件
with open("test_output.txt", "w", encoding="utf-8") as f:
    f.write("这是用 Python 写入的第一行文字。\n")
    f.write("Python 让文件操作变得很简单！\n")
    f.write(f"当前学习进度: 第10课\n")

print("文件 test_output.txt 已创建！")

# 读文件
with open("test_output.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容:")
    print(content)

# 按行读取
print("按行读取:")
with open("test_output.txt", "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, 1):
        print(f"  第{line_number}行: {line.strip()}")  # strip() 去掉末尾换行符
print()

# 文件模式说明:
# 'r' = 读取 (read)
# 'w' = 写入 (write)，会覆盖已有文件
# 'a' = 追加 (append)，在末尾添加
# 'r+' = 读写
print()


# ============================================================
#  第 11 课：异常处理 —— 让程序更健壮
# ============================================================

print("=" * 50)
print("第 11 课：异常处理 (try / except)")
print("=" * 50)

# 有时候程序会出错，用 try/except 来优雅地处理


def safe_divide(a, b):
    """安全除法，处理除零错误"""
    try:
        result = a / b
        return f"{a} / {b} = {result}"
    except ZeroDivisionError:
        return "错误：除数不能为零！"
    except TypeError:
        return "错误：请输入数字！"


print(safe_divide(10, 2))    # 正常
print(safe_divide(10, 0))    # 除零错误
print(safe_divide(10, "a"))  # 类型错误
print()

# try/except/else/finally 完整结构
print("完整异常处理示例:")
try:
    num = int("abc")  # 这会出错！
except ValueError as e:
    print(f"  捕获到错误: {e}")
else:
    print("  没有错误时执行这里")
finally:
    print("  无论是否出错，finally 都会执行")
print()


# ============================================================
#  第 12 课：综合小练习
# ============================================================

print("=" * 50)
print("第 12 课：综合练习 —— 简易学生成绩管理器")
print("=" * 50)


def student_grade_manager():
    """
    一个简单的学生成绩管理器
    演示了 列表、字典、循环、函数、条件判断 的综合使用
    """
    students = [
        {"姓名": "张三", "语文": 85, "数学": 92, "英语": 78},
        {"姓名": "李四", "语文": 90, "数学": 88, "英语": 95},
        {"姓名": "王五", "语文": 72, "数学": 65, "英语": 80},
        {"姓名": "赵六", "语文": 95, "数学": 97, "英语": 93},
    ]

    print("\n>> 学生成绩单")
    print("-" * 40)

    # 遍历每个学生
    for student in students:
        name = student["姓名"]
        chinese = student["语文"]
        math = student["数学"]
        english = student["英语"]

        # 计算平均分
        average = (chinese + math + english) / 3

        # 判断等级
        if average >= 90:
            level = "** 优秀"
        elif average >= 80:
            level = "^^ 良好"
        elif average >= 60:
            level = "-- 及格"
        else:
            level = "!! 加油"

        # 输出
        print(f"{name}: 平均分 {average:.1f}  {level}")
        print(f"    语文{chinese} | 数学{math} | 英语{english}")

    print("-" * 40)

    # 统计全班平均分
    all_scores = []
    for student in students:
        all_scores.append((student["语文"] + student["数学"] + student["英语"]) / 3)

    class_average = sum(all_scores) / len(all_scores)
    print(f"  全班平均分: {class_average:.1f}")

    # 找出最高分
    best_student = max(students, key=lambda s: (s["语文"] + s["数学"] + s["英语"]) / 3)
    print(f"  最高分: {best_student['姓名']} ({(best_student['语文'] + best_student['数学'] + best_student['英语']) / 3:.1f}分)")
    print()


# 运行综合练习
student_grade_manager()


# ============================================================
#  第 13 课：Python 常用小技巧
# ============================================================

print("=" * 50)
print("第 13 课：实用小技巧")
print("=" * 50)

# --- 列表推导式 —— 一行代码生成列表 ---
squares = [x ** 2 for x in range(1, 11)]  # 1到10的平方
print(f"1到10的平方: {squares}")

even_numbers = [x for x in range(1, 21) if x % 2 == 0]  # 1-20中的偶数
print(f"1-20中的偶数: {even_numbers}")

# --- 字典推导式 ---
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"单词长度: {word_lengths}")

# --- zip() 同时遍历多个列表 ---
names = ["张三", "李四", "王五"]
ages = [18, 19, 20]
for name, age in zip(names, ages):
    print(f"  {name}: {age}岁")

# --- enumerate() 带索引遍历 ---
print("倒计时排行榜:")
ranking = ["第一名", "第二名", "第三名"]
for rank, title in enumerate(ranking, 1):
    print(f"  {rank}. {title}")

print()

