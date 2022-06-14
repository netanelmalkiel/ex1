def nati_mal(start, end):
    for number in range(starting_num, ending_num):
        if number % 3 == 0 and number % 5 == 0:
            print('nati malkiel')
        elif number % 3 == 0:
            print('nati')
        elif number % 5 == 0:
            print('malkiel')
        else:
            print(number)


starting_num = int(input("give me a starting number: "))
ending_num = int(input("give me a ending number: "))

nati_mal(starting_num, ending_num)



# def nati_mal(s_num, e_num):
#     for number in range(s_num, e_num):
#         if number % 3 == 0 and number % 5 == 0:
#             print('nati malkiel')
#         elif number % 3 == 0:
#             print('nati')
#         elif number % 5 == 0:
#             print('malkiel')
#         else:
#             print(number)
#
#
# nati_mal(1, 31)