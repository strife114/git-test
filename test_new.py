"""
测试模块
"""


def test_basic():
    """基础测试用例"""
    assert 1 + 1 == 2


def test_string():
    """字符串测试用例"""
    result = "Hello, Git!"
    assert isinstance(result, str)
    assert len(result) > 0


if __name__ == "__main__":
    test_basic()
    test_string()
    print("sss")