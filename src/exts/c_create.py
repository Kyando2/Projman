from .u_read import read

def handler(args, gb):
    data = read(gb + "\\config\\environment.kya")
    if data:
        environment = data['environments'][data['current']]
        print(environment)
    else:
        print("No environments found, please use projman init")
        sys.exit()