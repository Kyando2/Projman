import os
import sys
import Kyandle

def handler(args, gb):
    if not args.d:
        wkdir = os.getcwd()
        to_create = os.path.join(wkdir, "Projects")
        if not os.path.exists(to_create):
            os.mkdir(to_create)
        project_dir = to_create
    else:
        project_dir = args.d

    if not os.path.isdir(project_dir):
        print('The path specified does not exist')
        sys.exit()

    has = {"archive": False, "experimentation": False, "current": False}
    for filename in os.listdir(project_dir):
        if str.lower(filename) in has.keys():
            has[str.lower(filename)] = True

    __create_files(project_dir, has)
    __generate_environment(args.name, gb, project_dir)

    print("Successfully generated a project environment")

def __create_files(project_dir, has):

    if not has["archive"]:
        to_create = os.path.join(project_dir, "Archive")
        os.mkdir(to_create)

    if not has["experimentation"]:
        to_create = os.path.join(project_dir, "Experimentation")
        os.mkdir(to_create)

    if not has["current"]:
        to_create = os.path.join(project_dir, "Current")
        os.mkdir(to_create)

def __generate_environment(name, gb, directory):
    if os.path.exists(gb + "\\config\\environment.kya"):
        with open(gb + "\\config\\environment.kya", "r") as f:
            data = Kyandle.parse(f.read())

        if name in data["environments"]:
            print("Environment with a similar name already exists")
            sys.exit()

        data["current"] = name
        data["environments"][name] = {"projects": [], "metadata": {"directory": directory}}
    else:
        data = {"environments": {name: {"projects": [], "metadata": {"directory": directory}}}, "current": name}

    with open(gb + "\\config\\environment.kya", "w") as f:
        f.write(Kyandle.serialize(data))