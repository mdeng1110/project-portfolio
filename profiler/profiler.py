import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    #argument for list of sorting algorithms
    parser.add_argument('--sort', 
      help='list of sorting algorithms', 
      type=list)
    #argument set prints information to the console. 
    #if argument isn't set, then no output should be displayed.
    parser.add_argument('--info', 
      help='prints information to the console', 
      type=str)
    #argument for sort ascending or descending.
    #if left unspecified, the profile should sort ascending.
    parser.add_argument('--sort_order', 
      help='sort ascending or descending',
      default='ascending')
    #argument to write logs to.  If no path is specified, 
    #then the profiler shoudl log to the local directory.
    parser.add_argument('--write_logs', 
      help='write logs', 
      default='.')
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(args)

if __name__ == '__main__':
    main()