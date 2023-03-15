def test_1():
    print("test 1")
    test_2()


def test_2():
    print("test 2")


def test_3():
    test_1()
    test_2()

test_3()