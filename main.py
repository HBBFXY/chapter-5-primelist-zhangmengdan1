def PrimeList(N):
    # 用于存储小于 N 的质数
    primes = []
    # 遍历从 2 到 N - 1 的所有数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 只需要检查到 num 的平方根即可，减少计算量
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 将质数列表用空格连接成字符串并返回
    return " ".join(primes)
