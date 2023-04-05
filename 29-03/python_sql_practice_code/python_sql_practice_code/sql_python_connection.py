import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return cnx
    except Exception as e:
        print(f'failed to connect + {str(e)}')


# EXAMPLE 1
def get_all_records():
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"connected to DB: {db_name}")

        query = """SELECT * from abcreport"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:

        if (db_connection):
            db_connection.close()
            print("DB connection is closed")

# EXAMPLE 2

def calc_commission(sold_items, commission):
    sales = []

    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales) * (commission / 100)
    return commission


def get_all_records_for_rep(rep_name):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = f"""SELECT Item, Units, Total FROM abcdreport WHERE Rep = '{rep_name}"""
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

        cur.close()
        comp = round(calc_commission(result, commission=10), 2)

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    print("Commission for {} is £{}".format(rep_name, comp))
    return rep_name, comp


# EXAMPLE 3 - INSERT INTO TABLE

import datetime as dt

record = {
    'OrderDate': '2020-12-15',
    'Region': 'Central',
    'Rep': 'Johnson',
    'Item': 'post-it-notes',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}


def insert_new_record(record):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(record.keys()),
            record['OrderDate'],
            record['Region'],
            record['Rep'],
            record['Item'],
            record['Units'],
            record['UnitCost'],
            record['Total'],
        )

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception as e:
        print(f"Error: {str(e)}")
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB conncection is closed")


    print("Record added to DB")


def update_record(col, new_value, filter_col, filter_value):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = f""" UPDATE abcreport 
                    SET {col} = '{new_value}'
                    WHERE {filter_col} = {filter_value}'
                    
        """

        cur.execute(query)
        db_connection.commit()

        cur.close()

    except Exception as e:
        print(f"Error raised = {str(e)}")
        raise DbConnectionError("Failed to read from DB")
    finally:
        if(db_connection):
            db_connection.close()
            print('DB connection is closed')

def main():
    import mysql.connector
    #get_all_records()
    get_all_records_for_rep('Morgan')
    # insert_new_record(record)
    update_record(col = 'Item', new_value = 'Pencils', filter_col = 'Rep', filter_value = 'Fatma')

if __name__ == '__main__':
    main()
