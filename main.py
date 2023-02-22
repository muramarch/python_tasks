from modules import Todo, TodoItem


def main():
    my_todo = Todo()
    go_todo = Todo()

    my_task = TodoItem('Метод find должен принимать слово в качестве аргумента и выводить список экземпляров TodoItem, которые содержат это слово в виде кортежа, который будет иметь формат (индекс, экземпляр).')
    my_task2 = TodoItem('Приготовить покушать')

    my_todo.add_todo(my_task)
    my_task2.check()
    my_todo.add_todo(my_task2)

    my_todo.list_items()

    my_task2.uncheck()

    my_todo.list_items()

    print(my_todo.find('слово'))


if __name__ == '__main__':
    main()