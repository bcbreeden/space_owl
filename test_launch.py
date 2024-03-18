import unittest
from launch import get_all_launch_objects

class TestLaunch(unittest.TestCase):
    def test_get_all_launch_objs_count(self):
        launch_objs = get_all_launch_objects()
        self.assertGreater(len(launch_objs), 0)

if __name__ == '__main__':
    unittest.main()