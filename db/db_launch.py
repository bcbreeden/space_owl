import sqlite3

def create_launch_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Launches (
            launch_id INTEGER PRIMARY KEY,
            url TEXT,
            name TEXT,
            status_id INTEGER,
            status_name TEXT,
            status_description TEXT,
            net DATETIME,
            launch_service_provider_id INTEGER,
            launch_service_provider_url TEXT,
            launch_service_provider_name TEXT,
            launch_service_provider_type TEXT,
            rocket_id INTEGER,
            rocket_url TEXT,
            rocket_name TEXT,
            mission_id INTEGER,
            mission_name TEXT,
            mission_description TEXT,
            mission_type TEXT,
            mission_orbit_id INTEGER,
            mission_orbit_name TEXT,
            mission_orbit_abbrev TEXT,
            pad_location_id INTEGER,
            pad_location_name TEXT,
            pad_location_country_code TEXT
        )
    ''')

dummy_data = {
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

insert_statement = """
    INSERT OR REPLACE INTO Launches (
        launch_id, url, name, status_id, status_name, status_description, net, 
        launch_service_provider_id, launch_service_provider_url, launch_service_provider_name, launch_service_provider_type, 
        rocket_id, rocket_url, rocket_name, 
        mission_id, mission_name, mission_description, mission_type, 
        mission_orbit_id, mission_orbit_name, mission_orbit_abbrev, 
        pad_location_id, pad_location_name, pad_location_country_code
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

connection = sqlite3.connect('space_owl.db')
connection.row_factory = sqlite3.Row #this allows us to access the record details using the column headings from the row
cursor = connection.cursor()
create_launch_table(cursor)
cursor.execute(insert_statement, tuple(dummy_data.values()))

cursor.execute('SELECT * FROM Launches')
records = cursor.fetchall()
for record in records:
    print(record['pad_location_name'])
    print(len(records))
    print('----')
connection.commit()
connection.close()

