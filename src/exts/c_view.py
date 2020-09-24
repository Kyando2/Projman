import sys

from .u_read import read

def handler(args, gb):
    data = read(gb + "\\config\\environment.kya")
    if data:
        print("\n")
        [print(str(key) + ": " + value["metadata"]["directory"] + "\n\n") if not key == data["current"] else print(">> " + str(key) + ": " + value["metadata"]["directory"] + " <<\n\n") for key, value in data['environments'].items()]
    else:
        print("No environments found, please use projman init")
        sys.exit()

    