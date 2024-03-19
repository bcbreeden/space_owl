import unittest
from launch import get_all_launch_objects, get_demo_launch_obj
from db.db_launch import db_insert_into_launch_table, db_fetch_launch_by_id, db_delete_launch_by_id

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
        test_record = db_fetch_launch_by_id(demo_launch.launch_id)
        self.assertIsNotNone(test_record)
        self.assertEqual(test_record['launch_id'], demo_launch.launch_id)
        self.assertEqual(test_record['url'], demo_launch.url)
        self.assertEqual(test_record['name'], demo_launch.name)
        self.assertEqual(test_record['status_id'], demo_launch.status_id)
        self.assertEqual(test_record['status_name'], demo_launch.status_name)
        self.assertEqual(test_record['status_description'], demo_launch.status_description)
        self.assertEqual(test_record['net'], demo_launch.net)
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

if __name__ == '__main__':
    unittest.main()