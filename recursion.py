def funcThree():
    print('Three')


def funcTwo():
    funcThree()
    print('Two')


def funcOne():
    funcTwo()
    print('One')


funcOne()


# factorial

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)


print(fact(4))
