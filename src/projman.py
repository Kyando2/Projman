import argparse
import os
import sys

import Kyandle

from exts.c_init import handler as init_handler
from exts.c_switch import handler as switch_handler

dir = os.path.dirname(os.path.abspath(__file__))

def main():
    my_parser = argparse.ArgumentParser(description="Kyando's personal project manager")

    subparsers = my_parser.add_subparsers()

    parser_init = subparsers.add_parser('init')
    parser_init.add_argument("-d", "-directory", help="Directory for projects", default=None)
    parser_init.add_argument("name", help="Name of the projects environment")
    parser_init.set_defaults(func=init_handler)

    parser_switch = subparsers.add_parser('setenv')
    parser_switch.add_argument("name", help="Name of the environment")
    parser_switch.set_defaults(func=switch_handler)

    args = my_parser.parse_args()
    args.func(args, dir)

if __name__ == "__main__":
    main()