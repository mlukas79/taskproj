import pandas


class Scheduler:
    """A class to handle task log and their corresponding status."""

    def __init__(self):
        """Instantiates an object of Scheduler class."""

        self._tasklist = pandas.DataFrame()

    def print_tasks(self):
        return self._tasklist

    def add_task(self, task_content, status):
        """Returns a task list with an extra task added."""

        self._tasklist = self._tasklist.append(
        pandas.DataFrame.from_records([{'task': task_content, 'task_status': status}]),
                        ignore_index=True,
                        verify_integrity=False)
        #return self._tasklist

    def update_status(self, task_id, new_status):
        """Returns a task list with an updated tsa status."""

        self._tasklist.iloc[task_id]['task_status'] = new_status
        ##return self._tasklist

    def delete_task(self, task_id):
        """Returns a task list with a task removed."""

        self._tasklist = self._tasklist.drop(self._tasklist.index[task_id])
        return self._tasklist
