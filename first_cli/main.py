import argparse
import random


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--min', 
      help='returns smallest number of randomly generated list', 
      action='store_true')
    parser.add_argument('--max',
      help='returns largest number of randomly generated list',
      action='store_true')
    parser.add_argument('-n',
      help='length of the list', required=True, type=int)
    return parser.parse_args()

  
def max_num(array):
    """This function will return the maximum integer in the list

    Args:
        array (list): list of integers
    """
    max = 0
    for num in array:
        if num > max:
            max = num
    return max


def min_num(array):
    """This function will return the minimum integer in the list

    Args:
        array (list): list of integers
    """
    min = 999999999
    for num in array:
        if num < min:
            min = num
    return min


def main():
    args = parse_arguments()

    if not args.min and not args.max:
        print('PLEASE SET MINIMUM OR MAXIMUM FLAG')
        exit(1)
    elif args.n == 0:
        print('n NEEDS TO BE GREATER THAN 0')
        exit(1)
    
    array = [random.randint(-999999,999999) for i in range(args.n)]
    print('list: ', array)
    if args.min:
        print('minimum: ', min_num(array))
    if args.max:
        print('maximum: ', max_num(array))

if __name__ == '__main__':
    main()

