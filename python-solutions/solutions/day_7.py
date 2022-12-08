import sys
from typing import Dict

"""
Some constansts to easy reading
"""
COMMAND_TOKEN = "$"
CD = "cd"
LS = "ls"
DIR = "dir"
DIR_ABOVE = ".."
ROOT = "/"


class FileSystemNode:
    """
    This class represents a 'directory' in a file system. file_size 
    field represents total_size of 'files' inside that directory.
    child_paths represents the child paths (as String set). total_size
    represents the total size of the node. (files + child_paths)
    """

    def __init__(self, file_size=0):
        self.file_size = file_size
        self.child_paths = set()
        self.total_size = 0

    def __repr__(self):
        return f"file_size: {self.file_size}, child_paths: {self.child_paths}, total_size: {self.total_size}"


def calculate_folder_sizes(file_system: Dict, path: FileSystemNode) -> int:
    """
    This function is used to calculate the total size of
    each individual folder recursively, given the file_system
    dictionary and the starting path it calculates each folder's
    total size under the given path and traverse down using
    child_path each FileSystemNode has.
    """
    child_paths_size = 0
    if len(path.child_paths) != 0:
        for child in path.child_paths:
            child_paths_size += calculate_folder_sizes(
                file_system, file_system[child])
    path.total_size = path.file_size + child_paths_size
    return path.total_size


def day_7(part_number: int) -> int:
    """
    Instead of using a tree structure, I prefered to keep
    entire file structure in a dictionary and calculate the
    total sizes traversing the dictionary.
    """
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

            # Handling Commands
            if tokens[0] == COMMAND_TOKEN:
                if tokens[1] == CD:
                    if tokens[2] == ROOT:
                        current_path = "/"
                    elif tokens[2] == DIR_ABOVE:
                        # Moving up in the file tree by removing the last
                        # directory from the current_path string
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
                directories[current_path].child_paths.add(dir_path)

            # Reading a file line
            else:
                file_name = f"{current_path}{tokens[1]}"

                # If the given file name is not visited before
                # add it to 'files' set. Additionally add its
                # size the current path's size
                if file_name not in files:
                    files.add(file_name)
                    directories[current_path].file_size += int(tokens[0])

    # Calculating folder sizes recursively
    calculate_folder_sizes(directories, directories["/"])
    day_7_1_solution = 0
    for node in directories.values():
        if node.total_size < 100000:
            day_7_1_solution += node.total_size

    # Print solution 1
    print(f"day_7_1_solution: {day_7_1_solution}")

    if part_number == 1:
        return day_7_1_solution
    elif part_number == 2:
        # Second part
        needed_space = directories["/"].total_size - 40000000
        minimum_size = sys.maxsize
        for key, value in directories.items():
            if value.total_size > needed_space and value.total_size < minimum_size:
                minimum_size = value.total_size

        # Print solution 2
        print(f"day_7_2_solution: {minimum_size}")
        return minimum_size
