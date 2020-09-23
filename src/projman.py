import argparse
import os
import sy
import kyandle
https://docs.python.org/3/library/argparse.html#sub-commands
def main():
    my_parser = argparse.ArgumentParser(description="Kyando's personal project manager")

    subparsers = my_parser.add_subparsers('Action')

    my_parser.add_argument('-p', '--path', type=str, help="Path of the directory")

    args = my_parser.parse_args()

    project_dir = args.path or os.getcwd()

    if not os.path.isdir(project_dir):
        print('The path specified does not exist')
        sys.exit()

if __name__ == "__main__":
    main()