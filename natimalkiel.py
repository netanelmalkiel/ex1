import sys


def first_number_to_division():
    first_number = input("give me the first number to check the division: ")
    if first_number.isdigit():
        print("ok")
    else:
        print("error")
        first_number = str(input("give me the first number to check the division: "))
        if first_number.isdigit():
            print("ok")
        else:
            sys.exit()

    return str(first_number)


def second_number_to_division():
    second_number = input("give me the second number to check the division: ")
    if second_number.isdigit():
        print("ok")
    else:
        print("error")
        second_number = str(input("give me the second number to check the division: "))
        if second_number.isdigit():
            print("ok")
        else:
            sys.exit()

    return str(second_number)


def the_answer(first_number, second_number):
    for number in range(1, 100):
        if number % int(first_number) == 0 and number % int(second_number) == 0:
            print('nati malkiel')
        elif number % int(first_number) == 0:
            print('nati')
        elif number % int(second_number) == 0:
            print('malkiel')
        else:
            print(number)


the_answer(first_number_to_division(), second_number_to_division())
