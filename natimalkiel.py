import sys

def numbers_to_check(fun):
    number = input(f"give me the {fun} number: ")
    if not number.isdigit():
         number = numbers_to_check(fun)

    return number

num1 = numbers_to_check("first")
num2 = numbers_to_check("second")


def the_answer(first_number, second_number):
    for number in range(1, 101):
        if number % int(first_number) == 0 and number % int(second_number) == 0:
            print('nati malkiel')
        elif number % int(first_number) == 0:
            print('nati')
        elif number % int(second_number) == 0:
            print('malkiel')
        else:
            print(int(number))


def writing(file_name):
    sys.stdout = open(file_name, 'w+')
    the_answer(num1, num2)
filename = input("name for the file: ")

the_answer(num1, num2)
writing(filename)

