from modules import Todo, TodoItem

def main():
    my_todo = Todo()
 
    while True:
        task = input("Add new task and press 'q' for break: ")
 
        if task == 'q':
            break
 
        my_task = TodoItem(task)
        my_todo.add_todo(my_task)
 
    my_todo.list_items()
 
    print(my_todo.find('Eating'))


if __name__ == '__main__':
    main()