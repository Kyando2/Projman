import os
import sys

import Kyandle

def handler(args, gb):
    if os.path.exists(gb + "\\config\\environment.kya"):
        with open(gb + "\\config\\environment.kya", "r") as f:
            data = Kyandle.parse(f.read())
        if args.name in data["environments"]:
            data["current"] = args.name
    else:
        print("Please run projman init before trying to switch env")
        sys.exit()

    with open(gb + "\\config\\environment.kya", "w") as f:
        f.write(Kyandle.serialize(data))
    
    print("Successfully changed environment")