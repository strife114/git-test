"""显示当前时间"""
from datetime import datetime


def show_time():
    """打印当前日期时间"""
    now = datetime.now()
    print(f"日期: {now.strftime('%Y-%m-%d')}")
    print(f"时间: {now.strftime('%H:%M:%S')}")
    print(f"星期: {['一','二','三','四','五','六','日'][now.weekday()]}")
    print(f"时间戳: {now.timestamp():.0f}")


if __name__ == "__main__":
    show_time()
