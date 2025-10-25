def isOdd(value):
    
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
