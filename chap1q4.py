import os

def list_directory_contents(path="."):
    """
    Print the names of all entries (files, folders, links, etc.) in the directory given by path.
    Default path is the current working directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: path '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: no permission to access '{path}'.")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    # Example: you can change this to any directory you want to list
    dir_to_list = input("Enter the path of the directory (press Enter for current directory): ").strip()
    if dir_to_list == "":
        dir_to_list = "."  # current directory
    list_directory_contents(dir_to_list)

