def nati_mal(s_num, e_num):
    for number in range(s_num, e_num):
        if number % 3 == 0 and number % 5 == 0:
            print('nati malkiel')
        elif number % 3 == 0:
            print('nati')
        elif number % 5 == 0:
            print('malkiel')
        else:
            print(number)


nati_mal(1, 31)



