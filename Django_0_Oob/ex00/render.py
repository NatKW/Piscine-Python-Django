import sys, os, re
import settings

def main():
    if (len(sys.argv) != 2):
        return print("Please =) Usage: python3 render.py myCV.template")
    path = sys.argv[1]
    regex = re.compile(".*\.template")
    if not regex.match(path):
        return print("Bad file extension. Please use file <.template>")
    if not os.path.isfile(path):
        return print("file does not exist : {}".format(path))
    f = open(path, "r")
    template = "".join(f.readlines())
    f.close()
    file = template.format(
        first_name=settings.first_name, last_name=settings.last_name,
        age=settings.age, job=settings.job)
    regex = re.compile("(\.template)")
    path = "".join([path[0:regex.search(path).start()], ".html"])
    f = open(path, "w")
    f.write(file)
    f.close()

if __name__ == '__main__':
    main()