import os
from tkinter import *
from tkinter.filedialog import askdirectory


def Main():

    Tk().withdraw()  # use to hide tkinter window
    Dir = askdirectory(title="Select Folder")  # shows dialog box and return the path
    Printer(Dir)


def Printer(Dir, GIGABYTES_IN_MEGABYTES=1024):

    print("LOADING...")  # Sometimes it takes long to output results, this just indicates that the program is working and not broken
    sort_dict = Sorter(Dir)  # Give the directory as an input
    print("\n-SORTED-\n")
    for i in sort_dict:
        if i[1] > 1:  # continues using gigabytes
            fixed_float = float("{:.3f}".format(i[1]))
            data_type = "GB:   "
        elif i[1] < 0:  # no acces
            print(f"NO ACCES : {i[0]}")
            continue
        else:  # convert to megabytes
            mega_float = i[1] * GIGABYTES_IN_MEGABYTES
            fixed_float = float("{:.3f}".format(mega_float))
            data_type = "MB:   "

        dflt_white_space = 8
        white_space = " " * (dflt_white_space - len(str(fixed_float)))
        print(f"{fixed_float}  {white_space + data_type + i[0]}")

    if input("\nPress 'r' to retry, press anything else to exit\n") == "r":
        Main()


def get_dir_size(Dir):  # Returns the `directory` size in bytes

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
        return -1  # returns a negative size that will be visible (to use conditions) after the conversion
    return total


def get_subdirs(Dir):

    dir_array = os.listdir(Dir)
    return dir_array


def Sorter(Dir, GIGABYTES_IN_BYTES=1073741824):

    Dict = {}
    dir_array = get_subdirs(Dir)

    for x in range(len(dir_array)):
        file_size = float(get_dir_size(Dir + "\\" + dir_array[x])) / GIGABYTES_IN_BYTES  # Converts the bytes to GB

        Dict[dir_array[x]] = file_size

    sort_dict = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
    return sort_dict


if __name__ == "__main__":
    Main()
