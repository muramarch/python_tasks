from modules import Todo, TodoItem

def main():
    my_todo = Todo()
    go_todo = Todo()

    my_task = TodoItem('The find method should take a word as an argument and output a list of TodoItem instances that contain this word as a tuple, which will have the format (index, instance).')
    my_task2 = TodoItem('Prepare to eat')

    my_todo.add_todo(my_task)
    my_task2.check()
    my_todo.add_todo(my_task2)

    my_todo.list_items()

    my_task2.uncheck()

    my_todo.list_items()

    print(my_todo.find('word'))

if __name__ == '__main__':
    main()