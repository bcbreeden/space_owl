def get_test_launch_data():
    # Dummy data for a launch object
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