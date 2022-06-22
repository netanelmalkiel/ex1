import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='dividing numbers')
    parser.add_argument('--first', type=int, required=True, help='enter the first number')
    parser.add_argument('--second', type=int, required=True, help='enter the second number')
    args = parser.parse_args()
    sys.stdout.write(str(the_answer(args)))


def the_answer(args):
    for number in range(1, 31):
        if number % int(args.first) == 0 and number % int(args.second) == 0:
            print('nati malkiel')
        elif number % int(args.first) == 0:
            print('nati')
        elif number % int(args.second) == 0:
            print('malkiel')
        else:
            print(int(number))


def writing(file_name):
    sys.stdout = open(file_name, 'w+')
    main()


filename = input("name for the file: ")

if __name__ == '__main__':
    main()
    writing(filename)
