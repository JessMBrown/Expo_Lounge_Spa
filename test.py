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

# Example 1: Get all the records


def get_all_records():
    try:
        db_name = 'spa'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to Db: {db_name}")

        query = """SELECT * FROM Spa_Booking"""
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
#
#
# # Example 2: Get all the records for a sales rep and calculate their commission
#
# def calc_commission(sold_items, commission):
#     sales = []
#
#     for item in sold_items:
#         sales.append(item[2])
#
#     rep_commission = sum(sales)*(commission/100)
#     return rep_commission
#
#
# def get_all_records_for_rep(rep_name):
#     try:
#         db_name = 'tests'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f"Connected to Db: {db_name}")
#
#         query = f"""SELECT Item, Units, Total from abcreport WHERE Rep = '{rep_name}'"""
#         cur.execute(query)
#
#         result = cur.fetchall()
#         for i in result:
#             print(i)
#
#         commission = f"£{round(calc_commission(result, 10), 2)}"
#         print(commission)
#
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError("Failed to read data from DB")
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")
#
#
# # Example 3: Insert new record
#
# record_to_add = {
#     'OrderDate': '2024-06-20',
#     'Region': 'Central',
#     'Rep': 'Johnson',
#     'Item': 'post-it-notes',
#     'Units': 220,
#     'UnitCost': 2.5,
#     'Total': 220*2.5
# }
#
#
# def insert_new_record(record):
#     try:
#         db_name = 'tests'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f"Connected to Db: {db_name}")
#
#         print(', '.join(record.keys()))
#
#         query = f"""INSERT INTO abcreport ({', '.join(record.keys())})
#                 VALUES (
#                     '{record['OrderDate']}',
#                     '{record['Region']}',
#                     '{record['Rep']}',
#                     '{record['Item']}',
#                     {record['Units']},
#                     {record['UnitCost']},
#                     {record['Total']})"""
#
#         cur.execute(query)
#         db_connection.commit()
#         print(f"New Record added to database")
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError("Failed to write data to DB")
#     finally:
#         if db_connection:
#             db_connection.close()
#             print("DB connection is closed")


def main():
    get_all_records()
    # get_all_records_for_rep('Jones')
    # insert_new_record(record_to_add)


if __name__ == '__main__':
    main()
