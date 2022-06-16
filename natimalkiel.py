import sys


def nati_malkiel(range_first_number, range_second_number):
    number_1_to_check = str(input("give me the first number to check the division: "))
    if number_1_to_check.isdigit():
        print("ok")
    else:
        print("error")
        (input("give me the first number to check the division: "))
        sys.exit()
    number_2_to_check = str(input("give me the second number to check the division: "))
    if number_2_to_check.isdigit():
        print("ok")
    else:
        print("error")
        str(input("give me the second number to check the division: "))
        sys.exit()

    for number in range(range_first_number, range_second_number):
        if number % int(number_1_to_check) == 0 and number % int(number_2_to_check) == 0:
            print('nati malkiel')
        elif number % int(number_1_to_check) == 0:
            print('nati')
        elif number % int(number_2_to_check) == 0:
            print('malkiel')
        else:
            print(number)


(nati_malkiel(1, 101)) # למה אני צריך לשים פה הוא לא עושה כלום




