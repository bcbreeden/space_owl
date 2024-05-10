from db.db_launch import db_get_all_launches, db_insert_into_launch_table, db_get_launches_after_now
from api.api import make_api_call
from datetime import datetime

class Launch:
    '''
    Launch objects contain all of the data for a specific launch mission. This class, and the subsequent functions, will act as the controller.
    '''
    def __init__(self, launch_id, url, name, status_id, status_name, status_description, net, launch_service_provider_id, launch_service_provider_url, launch_service_provider_name, launch_service_provider_type, rocket_id, rocket_url, rocket_name, mission_id, mission_name, mission_description, mission_type, mission_orbit_id, mission_orbit_name, mission_orbit_abbrev, pad_location_id, pad_location_name, pad_location_country_code):
        self.launch_id = launch_id
        self.url = url
        self.name = name
        self.status_id = status_id
        self.status_name = status_name
        self.status_description = status_description
        self.net = datetime.fromisoformat(net.replace('Z', '+00:00'))
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
    '''
    Queries the database for all launch entries and converts them into Launch objects.

    Returns: List of Launch objects.
    '''
    records = db_get_all_launches()
    all_launch_objects = []
    for record in records:
        all_launch_objects.append(_cast_db_record_to_object(record))
    return all_launch_objects

def get_launches_after_now(num_launches=5):
    '''
    Requests data from the database for a number of launches that are scheduled after the current time.
    '''
    print('Attempting to get all launches after the current time.', flush=True)
    records = db_get_launches_after_now(num_launches)
    launch_objects = []
    for record in records:
        launch_objects.append(_cast_db_record_to_object(record))
    return launch_objects

def get_demo_launch_obj():
    '''
    Returns: A demo Launch object used for testing.
    '''
    print('Configuring and returning a demo launch object.', flush=True)
    demo_launch = Launch (
        launch_id="abc112",
        url="https://example.com/launch1",
        name="Dummy Launch 123",
        status_id=1,
        status_name="Scheduled",
        status_description="Launch is scheduled",
        net="2100-12-31T00:00:00Z",
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

def build_historic_launch_data(next_api_tag=""):
    '''
    Self contained function that will call and iterate through the api to add all records to the database. The api returns 10 results at a time.

    Args: next_api_tag -> The api has a field that points to the next page of results.
    '''
    api_endpoint = 'launch' + next_api_tag
    data = make_api_call(endpoint=api_endpoint)[1]
    try:
        launch_results = data['results']
    except:
        print('Error finding results.', flush=True)
        print('Endpoint:', api_endpoint)
        return
    for result in launch_results:
        try:
            obj = _cast_api_result_to_object(result)
        except Exception as e:
            print('Exception while trying to cast into a launch object.', flush=True)
            print(e, flush=True)
            continue
        db_insert_into_launch_table(obj)
    data_next = data['next']
    try:
        index = data_next.find("/launch")
    except AttributeError:
        print('Next page not found. Ending historic data function.', flush=True)
        return
    next_page = data_next[index + len("/launch"):]
    build_historic_launch_data(next_api_tag=next_page)

    
def _cast_db_record_to_object(record):
    '''
    Takes in a record from the db and casts the data into a Launch object.
    '''
    print('Converting database record to launch object.', flush=True)
    print(record['launch_id'])
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
    '''
    Takes in a result entry from the api and casts the data into a Launch object.
    '''
    print('Converting api result to launch object.', flush=True)
    print(api_result['id'])
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

print(get_launches_after_now())