Filepath = "data.txt"
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


def get_todos(filepath=Filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_arg, filepath=Filepath):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

print("Hello from functions: ")