import unittest
from source import Scheduler
import pandas

scheduler = Scheduler()


class TestScheduler(unittest.TestCase):
    """A class to unit test Scheduler class."""


    def test_attribute_instance(self):
        """Sanity check if instantiation is correct."""

        self.assertIsInstance(
        Scheduler()._tasklist,
        pandas.core.frame.DataFrame
        )

    def test_add_task(self):
        """Test if adding task method adds correct values."""

        data = {'task': 'test your code',
                'task_status': 'in progress'
               }
        test_statement = scheduler.add_task(
            task_content=data['task'],
            status=data['task_status'])
        test_statement = scheduler._tasklist.values.all()
        result = pandas.DataFrame.from_records([data]).values.all()
        self.assertEqual(test_statement, result)

    def test_update_status(self):
        """Tests if the status of a task is updated correctly"""
        #assert scheduler._tasklist['task'].values.all() == ['test your code', 'test your code again']
        scheduler.update_status(
            task_id=0,
            new_status='still testing')
        result = scheduler._tasklist['task_status'].values.all()
        self.assertEqual(result, 'still testing')

    def tyest_delete_task(self):
        """Test if the task is deleted correctly"""

        assert scheduler._tasklist.values.shape == (1,2)
        scheduler.add_task(
            task_content='test task deletion',
            status='almost done')
        self.assertEqual(scheduler._tasklisat.values.shape, (1,2))


if __name__ == '__main__':
    unittest.main()
