FILEPATH = "todos.txt"


def get_todos(filepath='todos.txt'):
    try:
        with open(filepath, 'r') as get_file:
            todos = get_file.readlines()
        return todos
    except FileNotFoundError:
        print(f"File '{filepath}' not found. Creating a new file...")
        # Create the file and return an empty list
        with open(filepath, 'w') as new_file:
            pass  # Creating an empty file
        return []


def write_todos(todos_arg, filepath=FILEPATH):
    """
        Write a list of to-do items to a text file.
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
