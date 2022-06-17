def first_number_to_check():
    first_number = input("give me the first number to check: ")
    if first_number.isdigit():
        print("ok")
    else:
        return first_number_to_check()

    return first_number


def second_number_to_check():
    second_number = input("give me the first number to check: ")
    if second_number.isdigit():
        print("ok")
    else:
        return second_number_to_check()

    return second_number


def the_answer(first_number, second_number):
    for number in range(1, 100):
        if number % int(first_number) == 0 and number % int(second_number) == 0:
            print('nati malkiel')
        elif number % int(first_number) == 0:
            print('nati')
        elif number % int(second_number) == 0:
            print('malkiel')
        else:
            print(int(number))


first = first_number_to_check()
second = second_number_to_check()

the_answer(first, second)
