def isOdd(value):
    """
    判断输入是否为奇整数
    参数:
    value - 任意类型的输入值
    返回:
    bool - 如果是整数且为奇数返回 True，否则返回 False
    """
    # 判断类型是否为整数
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        if value % 2 != 0:
            return True
        else:
            return False
    else:
        return False

# 主程序部分，用于测试isOdd函数
if __name__ == "__main__":
    N = input()
    num = isOdd(N)
    print(num)
