class Todo:
    text_file = open('text.txt', 'a')
    def __init__(self):
        self.todo_items = []

    def add_todo(self, item):
        if not isinstance(item, TodoItem):
            return
        self.todo_items.append(item)

    def list_items(self):
        q = 0

        for i in self.todo_items:
            print(f"{q}. {i} - {i.is_done}")
            q += 1
            self.text_file.write(f"{q}. {i} - {i.is_done}\n")

    def find(self, word):
        find_item = []
        for i, item in enumerate(self.todo_items):
            if word in item.task:
                find_item.append((i, item))
        return find_item

        
class TodoItem:
    def __init__(self, task):
        self.task = task
        self.is_done = False

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False

    def __repr__(self):
        return self.task