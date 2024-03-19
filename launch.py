from db.db_launch import db_get_all_launches, db_insert_into_launch_table
from api.api import make_api_call

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

def get_demo_launch_obj():
    demo_launch = Launch (
        launch_id="abc112",
        url="https://example.com/launch1",
        name="Dummy Launch 123",
        status_id=1,
        status_name="Scheduled",
        status_description="Launch is scheduled",
        net="2024-03-10 12:00:00",
        launch_service_provider_id=1,
        launch_service_provider_url="https://example.com/provider1",
        launch_service_provider_name="SpaceX",
        launch_service_provider_type="Commercial",
        rocket_id=1,
        rocket_url="https://example.com/rocket1",
        rocket_name="Falcon 9",
        mission_id=1,
        mission_name="Dummy Mission 1",
        mission_description="This is a dummy mission",
        mission_type="Satellite Deployment",
        mission_orbit_id=1,
        mission_orbit_name="Low Earth Orbit",
        mission_orbit_abbrev="LEO",
        pad_location_id=1,
        pad_location_name="Kennedy Space Center",
        pad_location_country_code="US"
        )
    return demo_launch

def build_historic_launch_data():
    '''
    Self contained function that will call and iterate through the api to add records to the database.
    '''
    # make api call
    # get the next api call
    # iterate through the results
    # add each result to the database
    # call next
    # repeat
    data = make_api_call(endpoint='launch')[1]
    next = data['next']
    launch_results = data['results']
    for result in launch_results:
        obj = _cast_api_result_to_object(result)
        db_insert_into_launch_table(obj)
        

    
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

def _cast_api_result_to_object(api_result):
    launch_obj = Launch(
        launch_id=api_result['id'],
        url=api_result['url'],
        name=api_result['name'],
        status_id=api_result['status']['id'],
        status_name=api_result['status']['name'],
        status_description=api_result['status']['description'],
        net=api_result['net'],
        launch_service_provider_id=api_result['launch_service_provider']['id'],
        launch_service_provider_url=api_result['launch_service_provider']['url'],
        launch_service_provider_name=api_result['launch_service_provider']['name'],
        launch_service_provider_type=api_result['launch_service_provider']['type'],
        rocket_id=api_result['rocket']['id'],
        rocket_url=api_result['rocket']['configuration']['url'],
        rocket_name=api_result['rocket']['configuration']['name'],
        mission_id=api_result['mission']['id'],
        mission_name=api_result['mission']['name'],
        mission_description=api_result['mission']['description'],
        mission_type=api_result['mission']['type'],
        mission_orbit_id=api_result['mission']['orbit']['id'],
        mission_orbit_name=api_result['mission']['orbit']['name'],
        mission_orbit_abbrev=api_result['mission']['orbit']['abbrev'],
        pad_location_id=api_result['pad']['id'],
        pad_location_name=api_result['pad']['location']['name'],
        pad_location_country_code=api_result['pad']['location']['country_code']
    )
    return launch_obj
