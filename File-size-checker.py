import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


def Main():
    Dir = askdirectory(title="Select Folder")  # shows dialog box and return the path
    sort_dict = Sorter(Dir)  # Give the directory as an input

    print("-Values in GB-\n")
    for i in sort_dict:
        if i[1] < 0:
            print(f"NO ACCES : {i[0]}")
        else:
            print(f"{i[1]} : {i[0]}")

    input("\nPress enter to exit")  # Exit program


def get_dir_size(Dir):  # Returns the `directory` size in bytes.
    total = 0
    try:
        for entry in os.scandir(Dir):  # print("[+] Getting the size of", directory)
            if entry.is_file():  # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():  # if it's a directory, recursively call this function
                total += get_dir_size(entry.path)
    except NotADirectoryError:  # if `directory` isn't a directory, get the file size
        return os.path.getsize(Dir)
    except PermissionError:  # if for whatever reason we can't open the folder, return -1
        return -999999  # returns a negative size that will be visible after the conversion
    return total


def get_subdirs(Dir):
    dir_array = []
    for x in os.listdir(Dir):
        dir_array.append(x)
    return dir_array


def Sorter(Dir):

    Dict = {}
    dir_array = get_subdirs(Dir)

    for x in range(len(dir_array)):
        file_size = float(get_dir_size(Dir + "\\" + dir_array[x])) / 1073741824  # Converts the bytes to GB
        formatted_float = "{:.3f}".format(file_size)
        Dict[dir_array[x]] = float(formatted_float)

    sort_dict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    return sort_dict


if __name__ == "__main__":
    Main()

