import sys


# checking the numbers to insert the function "the answer"
def numbers_to_check(number):
    if number.isdigit():
        print("ok")
    else:
        print("error")
        return numbers_to_check(input("give me number to check: "))

    return number


num1 = numbers_to_check(input("give me number1 to check: "))
num2 = numbers_to_check(input("give me number2 to check: "))


# checking the numbers to insert the function "determine_range"
def determine_range(range_number):
    if range_number.isdigit():
        print("ok")
    else:
        print("error")
        return determine_range(input("give me range number: "))

    return range_number


range1 = numbers_to_check(input("give me range to check: "))
range2 = numbers_to_check(input("give me range to check: "))


def the_answer(first_number, second_number, range1, range2):
    range_num = range(int(range1), int(range2))
    for number in range_num:
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
    the_answer(num1, num2, range1, range2)
filename = input("name for the file: ")

the_answer(num1, num2, range1, range2)
writing(filename)

