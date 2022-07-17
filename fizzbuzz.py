import sys


def numbers_to_check(position):
    number = input(f"give me the {position} number: ")
    if not number.isdigit():
        number = numbers_to_check(position)

    return number


num1 = numbers_to_check("first")
num2 = numbers_to_check("second")


def the_answer():
    for number in range(1, 101):
        if number % int(first_number) == 0 and number % int(second_number) == 0:
            print('fizz buzz')
        elif number % int(first_number) == 0:
            print('fizz')
        elif number % int(second_number) == 0:
            print('buzz')
        else:
            print(int(number))


first_number = num1
second_number = num2


def writing(file_name):
    sys.stdout = open(file_name, 'w+')
    the_answer()


filename = input("name for the file: ")


def main():
    the_answer()
    writing(filename)


if __name__ == '__main__':
    main()
