import sqlite3

def create_launch_table(cursor, connection):
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
    connection.commit()

def insert_into_launch_table(cursor, connection, data):
    '''
    This insert statement assumes all data points/features are present.
    '''
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
    cursor.execute(insert_statement, tuple(data.values()))
    connection.commit()

def get_all_launches(cursor, connection):
    '''
    Selects all data from the Launch table and returns the records.
    '''
    cursor.execute('SELECT * FROM Launches')
    connection.commit()
    return(cursor.fetchall())
