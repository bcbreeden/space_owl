from db.db_launch import db_get_all_launches

class Launch:
    def __init__(self, launch_id, url, name, status_id, status_name, status_description, net, launch_service_provider_id, launch_service_provider_url, launch_service_provider_name, launch_service_provider_type, rocket_id, rocket_url, rocket_name, mission_id, mission_name, mission_description, mission_type, mission_orbit_id, mission_orbit_name, mission_orbit_abbrev, pad_location_id, pad_location_name, pad_location_country_code):
        self.launch_id = launch_id
        self.url = url
        self.name = name
        self.status_id = status_id
        self.status_name = status_name
        self.status_description = status_description
        self.net = net
        self.launch_service_provider_id = launch_service_provider_id
        self.launch_service_provider_url = launch_service_provider_url
        self.launch_service_provider_name = launch_service_provider_name
        self.launch_service_provider_type = launch_service_provider_type
        self.rocket_id = rocket_id
        self.rocket_url = rocket_url
        self.rocket_name = rocket_name
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.mission_description = mission_description
        self.mission_type = mission_type
        self.mission_orbit_id = mission_orbit_id
        self.mission_orbit_name = mission_orbit_name
        self.mission_orbit_abbrev = mission_orbit_abbrev
        self.pad_location_id = pad_location_id
        self.pad_location_name = pad_location_name
        self.pad_location_country_code = pad_location_country_code

def get_all_launch_objects():
    records = db_get_all_launches()
    all_launch_objects = []
    for record in records:
        all_launch_objects.append(_cast_db_record_to_object(record))
    return all_launch_objects

def get_demo_launch_data():
    data = {
        "launch_id":1,
        "url": "https://example.com/launch1",
        "name": "Dummy Launch 123",
        "status_id": 1,
        "status_name": "Scheduled",
        "status_description": "Launch is scheduled",
        "net": "2024-03-10 12:00:00",
        "launch_service_provider_id": 1,
        "launch_service_provider_url": "https://example.com/provider1",
        "launch_service_provider_name": "SpaceX",
        "launch_service_provider_type": "Commercial",
        "rocket_id": 1,
        "rocket_url": "https://example.com/rocket1",
        "rocket_name": "Falcon 9",
        "mission_id": 1,
        "mission_name": "Dummy Mission 1",
        "mission_description": "This is a dummy mission",
        "mission_type": "Satellite Deployment",
        "mission_orbit_id": 1,
        "mission_orbit_name": "Low Earth Orbit",
        "mission_orbit_abbrev": "LEO",
        "pad_location_id": 1,
        "pad_location_name": "Kennedy Space Center",
        "pad_location_country_code": "US"
    }
    return data
    
def _cast_db_record_to_object(record):
    launch_obj = Launch(
        launch_id=record['launch_id'],
        url=record['url'],
        name=record['name'],
        status_id=record['status_id'],
        status_name=record['status_name'],
        status_description=record['status_description'],
        net=record['net'],
        launch_service_provider_id=record['launch_service_provider_id'],
        launch_service_provider_url=record['launch_service_provider_url'],
        launch_service_provider_name=record['launch_service_provider_name'],
        launch_service_provider_type=record['launch_service_provider_type'],
        rocket_id=record['rocket_id'],
        rocket_url=record['rocket_url'],
        rocket_name=record['rocket_name'],
        mission_id=record['mission_id'],
        mission_name=record['mission_name'],
        mission_description=record['mission_description'],
        mission_type=record['mission_type'],
        mission_orbit_id=record['mission_orbit_id'],
        mission_orbit_name=record['mission_orbit_name'],
        mission_orbit_abbrev=record['mission_orbit_abbrev'],
        pad_location_id=record['pad_location_id'],
        pad_location_name=record['pad_location_name'],
        pad_location_country_code=record['pad_location_country_code']
    )
    return launch_obj
