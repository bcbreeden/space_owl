import unittest
from datetime import datetime, timezone
from launch import get_all_launch_objects, get_demo_launch_obj, get_launches_after_now
from db.db_launch import db_insert_into_launch_table, db_get_launch_by_id, db_delete_launch_by_id

class TestLaunch(unittest.TestCase):
    def test_get_all_launch_objs_count(self):
        '''
        Verifies the the get_all_launch_objects returns a list greater than 0.
        '''
        launch_objs = get_all_launch_objects()
        self.assertGreater(len(launch_objs), 0)

    def test_launch_record_insert(self):
        '''
        Verifies that a launch record can be successfully created in the database and then fetched from said database.
        '''
        demo_launch = get_demo_launch_obj()
        db_insert_into_launch_table(demo_launch)
        test_record = db_get_launch_by_id(demo_launch.launch_id)
        self.assertIsNotNone(test_record)
        self.assertEqual(test_record['launch_id'], demo_launch.launch_id)
        self.assertEqual(test_record['url'], demo_launch.url)
        self.assertEqual(test_record['name'], demo_launch.name)
        self.assertEqual(test_record['status_id'], demo_launch.status_id)
        self.assertEqual(test_record['status_name'], demo_launch.status_name)
        self.assertEqual(test_record['status_description'], demo_launch.status_description)
        self.assertEqual(datetime.fromisoformat(test_record['net'].replace('Z', '+00:00')), demo_launch.net)
        self.assertEqual(test_record['launch_service_provider_id'], demo_launch.launch_service_provider_id)
        self.assertEqual(test_record['launch_service_provider_url'], demo_launch.launch_service_provider_url)
        self.assertEqual(test_record['launch_service_provider_name'], demo_launch.launch_service_provider_name)
        self.assertEqual(test_record['launch_service_provider_type'], demo_launch.launch_service_provider_type)
        self.assertEqual(test_record['rocket_id'], demo_launch.rocket_id)
        self.assertEqual(test_record['rocket_url'], demo_launch.rocket_url)
        self.assertEqual(test_record['rocket_name'], demo_launch.rocket_name)
        self.assertEqual(test_record['mission_id'], demo_launch.mission_id)
        self.assertEqual(test_record['mission_name'], demo_launch.mission_name)
        self.assertEqual(test_record['mission_description'], demo_launch.mission_description)
        self.assertEqual(test_record['mission_type'], demo_launch.mission_type)
        self.assertEqual(test_record['mission_orbit_id'], demo_launch.mission_orbit_id)
        self.assertEqual(test_record['mission_orbit_name'], demo_launch.mission_orbit_name)
        self.assertEqual(test_record['mission_orbit_abbrev'], demo_launch.mission_orbit_abbrev)
        self.assertEqual(test_record['pad_location_id'], demo_launch.pad_location_id)
        self.assertEqual(test_record['pad_location_name'], demo_launch.pad_location_name)
        self.assertEqual(test_record['pad_location_country_code'], demo_launch.pad_location_country_code)
        db_delete_launch_by_id(demo_launch.launch_id)
    
    def test_3_launches_after_now(self):
        '''
        Verifies that three launch objects are fetched when an argument is provided. Additionally, verifies the objects datetime is after the current datetime.
        '''
        launch_objs = get_launches_after_now(3)
        date_time = launch_objs[0].net
        now = datetime.now(timezone.utc)
        self.assertTrue(date_time > now)
        self.assertEqual(len(launch_objs), 3)
    
    def test_default_launches_after_now(self):
        '''
        Verifies that five launch objects are fetched when no argument is provided. Additionally, verifies the objects datetime is after the current datetime.
        '''
        launch_objs = get_launches_after_now()
        date_time = launch_objs[0].net
        now = datetime.now(timezone.utc)
        self.assertTrue(date_time > now)
        self.assertEqual(len(launch_objs), 5)

if __name__ == '__main__':
    unittest.main()