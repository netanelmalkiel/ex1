def first_number_to_check(number):
    if number.isdigit():
        print("ok")
    else:
        return first_number_to_check(number)

    return number


def determine_range(range_number):
    if range_number.isdigit():
        print("ok")
    else:
        return determine_range(range_number)

    return range_number


def the_answer(first_number, second_number, starting_range, end_range):
    for number in range(int(starting_range), int(end_range)):
        if number % int(first_number) == 0 and number % int(second_number) == 0:
            print('nati malkiel')
        elif number % int(first_number) == 0:
            print('nati')
        elif number % int(second_number) == 0:
            print('malkiel')
        else:
            print(int(number))


number_one = first_number_to_check(str(input("give me number: ")))
number_two = first_number_to_check(str(input("give me number: ")))
range_one = determine_range(input("give me starting range: "))
range_two = determine_range(input("give me ending range: "))

the_answer(number_one, number_two, range_one, range_two)
