from DB import con, cur

'''
this file for class
'''


class CreateTask:
    '''
    creat task
    '''

    def __init__(self, t_id: int, name_task: str, description=None, deadline=None):
        self.t_id = t_id
        self.name_task = name_task
        self.description = description
        self.deadline = deadline

    def save(self):
        lst = 'l_' + str(self.t_id)
        tuple_for_save = (
            self.name_task,
            self.description,
            self.deadline
        )
        cur.execute(f" INSERT INTO {lst} VALUES (?, ?, ?)", tuple_for_save)
        con.commit()


class EditTask(CreateTask):
    '''
    edit task
    '''

    def __init__(self, t_id: int, name_task: str, description=None, deadline=None):
        super().__init__(t_id, name_task, description=None, deadline=None)

    def edit_task(self):
        print(self.name_task)
        if self.description:
            print(self.description)
        if self.deadline:
            print(self.deadline)


class ShowTaskList(CreateTask):
    '''
    Берем все таски из бд
    '''
    pass


class DeleteTask(CreateTask):
    '''
    delete task from db
    '''


def main():
    test = CreateTask(42, 'Create project', 'yes', '6.2.2021')
    test.save()
    d = EditTask
    d.edit_task(test)


if __name__ == "__main__":
    main()