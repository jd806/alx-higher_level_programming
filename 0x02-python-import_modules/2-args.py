#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args_len = len(args)
    if args_len == 0:
        print('0 arguments.')
    else:
        print('{:d} argument{}:'.format(args_len, 's' if args_len > 1 else ''))

        for index in range(args_len):
            print('{:d}: {}'.format(index, args[index]))
