import dis


def fn_zero():
    x = 3
    if x < 0:
        return 0
    return 1


def fn_loop():
    for i in range(10):
        print(i)


def fn_infinite_loop():
    while True:
        print(1)


def demo():
    print(dis.dis(fn_zero))
    print("=========================================")
    print(dis.dis(fn_loop))
    print("=========================================")
    print(dis.dis(fn_infinite_loop))
    print("=========================================")