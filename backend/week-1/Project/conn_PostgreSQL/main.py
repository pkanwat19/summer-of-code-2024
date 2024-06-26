import psycopg2
from config import config

def connect():
    Connection =   None
    try:
        params = config()
        print("Connecting to the postgreSQL database...")
        connection = psycopg2.connect(**params)

        # Create a cursor
        crsr = connection.cursor()
        print('PostgreSQL database version: ')
        crsr.execute('Select version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.')
if __name__ == "__main__":
    connect()