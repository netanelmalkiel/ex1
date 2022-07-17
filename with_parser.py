import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='dividing numbers')
    parser.add_argument('-f', '--first', type=int, required=True, help='enter the first number')
    parser.add_argument('-s', '--second', type=int, required=True, help='enter the second number')
    parser.add_argument('-fn', '--filename', type=str, required=True, help='enter the file name')
    args = parser.parse_args()
    the_answer(args)
    writing(args)


def the_answer(args):
    for number in range(1, 501):
        if number % int(args.first) == 0 and number % int(args.second) == 0:
            print('fizz buzz')
        elif number % int(args.first) == 0:
            print('fizz')
        elif number % int(args.second) == 0:
            print('buzz')
        else:
            print(int(number))


def writing(args):
    sys.stdout = open(args.filename, 'w+')
    the_answer(args)


if __name__ == '__main__':
    main()
