import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=db_name,
        auth_plugin='mysql_native_password'
    )
    return cnx


def get_all_treatments():
    treatments = []
    try:
        # create connection
        db_name = 'Spa'
        db_connection = _connect_to_db(db_name)
        # create curser
        cur = db_connection.cursor()
        print(f"Connected to the {db_name} database")

        query = """SELECT * 
        FROM treatments"""
        # use the curser to execute query
        cur.execute(query)
        treatments = availability = _map_values(cur.fetchall())
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return treatments


def get_all_booking_data():
    global db_connection
    try:
        # create connection
        db_name = 'Spa'
        db_connection = _connect_to_db(db_name)
        # create curser
        cur = db_connection.cursor()
        print(f"Connected to the {db_name} database")
        print(f"###############################################################################")
        print(f"Booking ID | Date of Treatment | Time of Treatment | Treatment ID | Employee ID")

        query = """SELECT * 
        FROM Spa_Booking"""
        # use the curser to execute query
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def _map_values(treatment_bookings):
    mapped = []
    for item in treatment_bookings:
        mapped.append({
            'Date of Treatment': item[0],
            'Time of Treatment': item[1],
            'Treatment ID': item[2]
        })
    return mapped


def get_booking_by_date(date):
    availability = []
    try:
        # create connection
        db_name = 'Spa'
        db_connection = _connect_to_db(db_name)
        # create curser
        cur = db_connection.cursor()
        print(f"Connected to the {db_name} database")
        print(f"####################################################")
        print(f"Date of Treatment | Time of Treatment | Treatment ID")

        query = f"""SELECT Date_of_Treatment, Time_of_Treatment, Treatment_ID 
        FROM Spa_Booking 
        WHERE Date_of_Treatment = '{date}'"""
        # use the curser to execute query
        cur.execute(query)

        availability = _map_values(cur.fetchall())
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability


def add_booking(Date_of_Treatment, Time_of_Treatment, Treatment_ID, Employee_ID):
    try:
        # create connection
        db_name = 'Spa'
        db_connection = _connect_to_db(db_name)
        # create curser
        cur = db_connection.cursor()

        query = f"""
        INSERT INTO Spa_Booking (Date_of_Treatment, Time_of_Treatment, Treatment_ID, Employee_ID)
        VALUES
        ('2024-06-01', '10:30:00', 1, 2)
        """
        cur.execute(query)

    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    # get_all_booking_data()
    print(get_booking_by_date("2024-06-01"))
