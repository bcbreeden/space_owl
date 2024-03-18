import unittest
import sqlite3
import os
from common import get_test_launch_data
from db.db_launch import create_launch_table, insert_into_launch_table, get_all_launches

class TestAPI(unittest.TestCase):
    def test_launch_table(self):
        '''
        Creates a launch table and inserts demo data. Will attempt to remove the test db.
        '''
        connection = _create_test_db()
        cursor = connection.cursor()
        create_launch_table(cursor, connection)
        insert_into_launch_table(cursor, connection, get_test_launch_data())
        records = get_all_launches(cursor, connection)
        for record in records:
            self.assertEqual(record['name'], 'Dummy Launch 123')
            self.assertEqual(record['mission_name'], 'Dummy Mission 1')
        connection.close()
        _delete_test_db()

def _create_test_db():
    connection = sqlite3.connect('unit_test.db')
    connection.row_factory = sqlite3.Row
    print("Unit test db created.", flush=True)
    return connection

def _delete_test_db():
    try:
        os.remove('unit_test.db')
        print('Unit test db successfully deleted.')
    except FileNotFoundError:
        print('Unit test db file not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    unittest.main()