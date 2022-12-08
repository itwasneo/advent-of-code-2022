import sys
import pprint

COMMAND_TOKEN = "$"
CD = "cd"
LS = "ls"
DIR = "dir"
DIR_ABOVE = ".."
ROOT = "/"
FILE = "file"


class FileSystemNode:
    def __init__(self, file_size=0, directories=set()):
        self.file_size = file_size
        self.directories = directories

    def __repr__(self):
        return f"file_size: {self.file_size}, directories: {self.directories}"


def day_7_1() -> int:
    result = 69

    with open("../input/input_7_1.txt") as fp:
        current_path = ""
        directories = dict()
        files = set()
        while True:
            line = fp.readline()
            if not line:
                break

            tokens = line.split(" ")

            # Removin LF at the end of each line
            tokens[-1] = tokens[-1].replace("\n", "")

            # Printing current path for testing
            # print(current_path)

            # Handling Commands
            if tokens[0] == COMMAND_TOKEN:
                if tokens[1] == CD:
                    if tokens[2] == ROOT:
                        current_path = "/"
                    elif tokens[2] == DIR_ABOVE:
                        current_path_tokens = current_path.split('/')[1:-2]
                        if len(current_path_tokens) == 0:
                            current_path = "/"
                        else:
                            current_path = f"/{'/'.join(current_path_tokens)}/"
                    else:
                        current_path = f"{current_path}{tokens[2]}/"

                    # If the given path is not visited before
                    # add it to 'directories' dictionary with
                    # 0 total size
                    if current_path not in directories:
                        directories[current_path] = FileSystemNode()
                elif tokens[1] == LS:
                    # Reading directory content
                    continue
                else:
                    print(
                        f"Unexpected behavior: Should be a command token\ntokens: {tokens}")
                    sys.exit(1)

            # Reading 'dir' line
            elif tokens[0] == DIR:
                # Adding 'new' directories when they are seen
                # to the current path's directories
                dir_path = f"{current_path}{tokens[1]}/"

                # Printing 'dir' lines for testing
                print(f"{current_path}-->{dir_path}")

                directories[current_path].directories.add(dir_path)
                # print(directories[current_path].directories)

            # Reading a file line
            else:
                file_name = f"{current_path}{tokens[1]}"

                # If the given file name is not visited before
                # add it to 'files' set. Additionally add its
                # size the current path's size
                if file_name not in files:
                    files.add(file_name)
                    # directories[current_path] += int(tokens[0])

    # With this approach, we calculate only total
    # size of 'files' as our directory size, we
    # are not including the directories inside the
    # directories.

    # Pretty print
    printer = pprint.PrettyPrinter(indent=2, sort_dicts=True)

    # Directories
    # printer.pprint(directories)

    # Specific Directory
    # printer.pprint(directories["/"])

    # Files
    # printer.pprint(files)

    return result
