from db.db_launch import db_create_launch_table

'''
Creates tables and sets up the app on a new install.
'''
if __name__ == "__main__":
    db_create_launch_table()