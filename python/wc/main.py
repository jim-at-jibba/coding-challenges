#!/usr/bin/env python3

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="ccwc", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "positional", metavar="str", nargs="?", help="A positional argument"
    )

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

    parser.add_argument(
        "-w",
        help="The number of words in each input file is written to the standard output.",
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
    count_words = args.w
    file_path = args.positional
    # print(f'positional = "{pos_arg}"')
    # print(f'count_bytes = "{count_bytes}"')

    if file_path:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                # file = open(pos_arg).read()

                byte_count = os.stat(file_path).st_size
                contents = file.read()
                lines_count = contents.split("\n")
                word_count = contents.split()
                if count_bytes:
                    print(f"{byte_count} {file_path}")

                elif count_lines:
                    print(f"{len(lines_count)} {file_path}")

                elif count_words:
                    print(f"{len(word_count)} {file_path}")

                else:
                    # This does not work as word_count comes out as 0. This is because the file has already been read
                    # byte_count = os.stat(file_path).st_size
                    # lines_count = file.readlines()
                    # word_count = file.read().split()
                    print(
                        f"{len(lines_count)} {len(word_count)} {byte_count} {file_path}"
                    )
    else:
        stdin = sys.stdin.read()
        lines = stdin.split("\n")
        words = stdin.split()
        characters = len(stdin)
        if count_bytes:
            print(f"{len(lines)}")
        elif count_lines:
            print(f"{characters}")
        elif count_words:
            print(f"{len(words)}")
        else:
            print(f"{len(lines)} {len(words)} {characters}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
