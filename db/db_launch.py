import sqlite3
from datetime import timezone

'''
This file serves as the primary entry point to the database. All functions should be self contained. That is, they should create independent connections and close them.
'''

def db_create_launch_table():
    '''
    Builds the launch table if it does not already exist.
    '''
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Launches (
            launch_id TEXT PRIMARY KEY,
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
    connection.close()

def db_insert_into_launch_table(launch):
    '''
    This insert statement assumes a launch object is being passed in.
    '''
    print(launch.launch_id, flush=True)
    print('Attempting to insert into the database.', flush=True)
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    net = launch.net
    net_utc = net.astimezone(timezone.utc)
    insert_statement = '''
    INSERT OR REPLACE INTO launches (launch_id, url, name, status_id, status_name, status_description, net, 
                            launch_service_provider_id, launch_service_provider_url, launch_service_provider_name, 
                            launch_service_provider_type, rocket_id, rocket_url, rocket_name, mission_id, 
                            mission_name, mission_description, mission_type, mission_orbit_id, mission_orbit_name, 
                            mission_orbit_abbrev, pad_location_id, pad_location_name, pad_location_country_code) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(insert_statement, (launch.launch_id, launch.url, launch.name, launch.status_id, launch.status_name, launch.status_description,
                         net_utc, launch.launch_service_provider_id, launch.launch_service_provider_url, launch.launch_service_provider_name,
                         launch.launch_service_provider_type, launch.rocket_id, launch.rocket_url, launch.rocket_name, launch.mission_id,
                         launch.mission_name, launch.mission_description, launch.mission_type, launch.mission_orbit_id, launch.mission_orbit_name,
                         launch.mission_orbit_abbrev, launch.pad_location_id, launch.pad_location_name, launch.pad_location_country_code))
    print('Successfully inserted into the database.', flush=True)
    connection.commit()
    connection.close()

def db_get_all_launches():
    '''
    Selects all data from the Launch table and returns the records.
    '''
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Launches''')
    records = cursor.fetchall()
    connection.commit()
    connection.close()
    return(records)

def db_get_launches_after_now():
    '''
    Selects all launches that have a NET after the current time.
    '''
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT *
                    FROM Launches
                    WHERE net > datetime('now', 'utc');
                   ''')
    records = cursor.fetchall()
    connection.commit()
    connection.close()
    return(records)

def db_get_launch_by_id(id):
    '''
    Selects a single launch record via the launch_id.
    '''
    print(id, flush=True)
    print('Attempting to fetch from the database', flush=True)
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM launches WHERE launch_id=?''', (id,))
    record = cursor.fetchone()
    connection.commit()
    connection.close()
    if record == None:
        print("Record not found:", id, flush=True)
    else:
        print('Record fetched successfully', flush=True)
        return(record)

def db_delete_launch_by_id(id):
    '''
    Deletes a single launch record via the launch_id.
    '''
    print(id, flush=True)
    print('Attempting to delete from the database', flush=True)
    connection = sqlite3.connect('space_owl.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM launches WHERE launch_id=?''', (id,))
    record = cursor.fetchone()
    if record == None:
        print("Record not found:", id, flush=True)
    else:
        cursor.execute('''DELETE FROM launches WHERE launch_id=?''', (id,))
        print('Record deleted successfully', flush=True)
    connection.commit()
    connection.close()
