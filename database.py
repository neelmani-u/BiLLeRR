# ------------ Importation ------------------
import sqlite3
# from main_bill import ITEMS



# ---------- Create Table ---------------
def create_table():
    con = sqlite3.connect('Database.db')
    cursor = con.cursor()
    try:

        query = '''CREATE TABLE Order_Details (
                Order_id      TEXT     NOT NULL,
                Customer_name TEXT     NOT NULL,
                Customer_phn  TEXT     NOT NULL,
                Date          DATETIME NOT NULL,
                Items         TEXT     NOT NULL,
                Quantity      INTEGER  NOT NULL,
                Total_amt     REAL     NOT NULL);'''

        cursor.execute(query)
        con.commit()
        print('Database Creation and Table Ceation Completed!')
        cursor.close()
    except:
        print('Error!')
    finally:
        if con:
            con.close()


# ----------------- Save Data -------------------
def save_data_into_db(data):
    con = sqlite3.connect('Database.db')
    cursor = con.cursor()
    try:

        query = '''INSERT INTO Order_Details
                (Order_id, Customer_name, Customer_phn, Date, Items, Quantity, Total_amt)
                VALUES (?, ?, ?, ?, ?, ?, ?);'''

        cursor.execute(query, data)
        con.commit()
        print('All Data Saved Successfully!')
        cursor.close()
    except Exception as e:
        print('Error!',e)
    finally:
        if con:
            con.close()


def get_data(code):
    con = sqlite3.connect('GUI\Items_Database.db')
    cursor = con.cursor()
    try:

        query = f'''SELECT * FROM Items_List WHERE item_code = {code};'''

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()


# ------------- Save Items List ------------------

def save_items_list():
    con = sqlite3.connect('Items_Database.db')
    cursor = con.cursor()
    try:
        # create Items Table
        query = '''CREATE TABLE Items_List (
                item_code      INTEGER  NOT NULL PRIMARY KEY,
                item_name      TEXT     NOT NULL,
                item_rate      INTEGER  NOT NULL,
                item_category  TEXT     NOT NULL);'''

        cursor.execute(query)
        con.commit()
        print('Table Items_List created successfully')
        
        # Inserting Items in tables

        query = '''INSERT INTO Items_List
                (item_code, item_name, item_rate, item_category)
                VALUES (?, ?, ?, ?);'''


        for item in ITEMS.items():
            for code in item[1].items():
                for item_name, item_rate in code[1].items():
                    data = (code[0], item_name, item_rate, item[0])
                    cursor.execute(query, data)

        con.commit()
        print('All Data saved successfully!')
        cursor.close()
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()


def get_items_list():
    con = sqlite3.connect('Items_Database.db')
    cursor = con.cursor()
    try:

        query = '''SELECT * FROM Items_List;'''

        cursor.execute(query)
        data = cursor.fetchall()
        row = 0
        col = 0
        for tup_data in data:
            row += 1
            col = 0
            for obj in tup_data:
                col += 1
        cursor.close()
        return row, col, data
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()


def user_db():
    con = sqlite3.connect('Database.db')
    cursor = con.cursor()
    try:

        query = '''CREATE TABLE UserManager (
                email       TEXT  NOT NULL,
                phoneNumber TEXT  NOT NULL,
                password    TEXT  NOT NULL,
                firstName   TEXT  NOT NULL,
                lastName    TEXT  NOT NULL);'''

        cursor.execute(query)
        con.commit()
        cursor.close()
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()


def store_data_in_userManager(data):
    con = sqlite3.connect('Database.db')
    cursor = con.cursor()
    try:

        query = '''INSERT INTO UserManager
                (email, phoneNumber, password, firstName, lastName)
                VALUES (?, ?, ?, ?, ?);'''

        cursor.execute(query, data)
        con.commit()
        cursor.close()
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()


def get_data_from_userManager(id, id_value):
    con = sqlite3.connect('Database.db')
    cursor = con.cursor()
    try:

        query = f'''SELECT * FROM UserManager WHERE {id} = {id_value}'''

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
    except Exception as e:
        print('Error!', e)
    finally:
        if con:
            con.close()

