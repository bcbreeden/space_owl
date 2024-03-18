from db.db_launch import get_all_launches

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
        pass