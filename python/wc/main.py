#!/usr/bin/env python3

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="ccwc", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("positional", metavar="str", help="A positional argument")

    parser.add_argument(
        "-c",
        help="The number of bytes in each input file is written to the standard output.",
        action="store_true",
    )

    parser.add_argument(
        "-l",
        help="The number of lines in each input file is written to the standard output.",
        action="store_true",
    )
    #
    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)
    #
    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)
    #
    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    # str_arg = args.arg
    # int_arg = args.int
    # file_arg = args.file
    count_bytes = args.c
    count_lines = args.l
    file_path = args.positional
    # print(f'positional = "{pos_arg}"')
    # print(f'count_bytes = "{count_bytes}"')

    if os.path.exists(file_path):
        # file = open(pos_arg).read()

        if count_bytes:
            count = os.stat(file_path).st_size
            print(f"{count} {file_path}")
            return
        if count_lines:
            with open(file_path, "r") as file:
                lines = file.readlines()
                print(f"{len(lines)} {file_path}")
            return

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
