# check digits
#
def check_digits():
    number = str(input("please give me the first number: "))

    if number.isdigit():
        print("ok")
    else:
        try_one = input(f"please give me a number, {number}! is not a number: ")
        if try_one.isdigit():
            print("ok")
        else:
            print("program end")

    number2 = str(input("please give me the second number: "))

    if number2.isdigit():
        print("ok")
    else:
        try_one = input(f"please give me a number, {number2}! is not a number: ")
        if try_one.isdigit():
            print("ok")
        else:
            print("program end")
#
#
# check_digits()

# range to check


def range_to_check(f_num, s_num):

    for x in range(f_num, s_num):
        print(x)

# numbers to check


def nati_mal(num3, num4):
    for x in range(1, 100):
        if x % num3 == 0 and x % num4 == 0:
            print('nati malkiel')
        elif x % num3 == 0:
            print('nati')
        elif x % num4 == 0:
            print('malkiel')
        else:
            print(x)











