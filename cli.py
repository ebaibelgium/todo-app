#from functions import get_todos, write_todo
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input("Enter:\n 'add' followed by the task to do, or\n"
                        "' show' to view the tasks, or\n'edit' followed by the number of the task to edit, or\n"
                        "'complete' followed by the number of the task to remove, or\n "
                        "'exit' to exit the program.:\n ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todo(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos('todos.txt')

        # new_todos = [todo.strip('\n') for todo in todos] # list comprehension
        # for index, todo in enumerate(new_todos):
        #     print(f"{index+1}-{todo.capitalize()}")

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            print(f"{index+1}-{todo.capitalize()}")

    elif user_action.startswith('edit'):
        try:
            number = user_action[5:]
            number = int(number)
            number = number-1

            todos = functions.get_todos()

            new_todo = input('Enter the new todo: ')
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_todo(todos)

        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('complete'):
        try:
            number = user_action[9:]
            number = int(number)

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.write_todo(todos)

            message = f"'{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid!')


print('Bye!')