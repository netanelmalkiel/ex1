def first_number_to_check(number):
    if number.isdigit():
        print("ok")
    else:
        return first_number_to_check(number)

    return number


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


one = first_number_to_check(str(input("give me number: ")))
two = first_number_to_check(str(input("give me number: ")))
the_answer(one, two)
