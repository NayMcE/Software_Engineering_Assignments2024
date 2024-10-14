import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx



def get_all_recipe_collection():
    db_connection = _connect_to_db()
    try:
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT recipe_name, meal_type FROM recipes"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_all_recipe_with_id():
    db_connection = _connect_to_db()
    try:
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT recipe_id, recipe_name, meal_type FROM recipes"""
        cur.execute(query)
        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_breakfast_recipes():
    db_connection = _connect_to_db()
    try:
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM recipes WHERE meal_type = 'breakfast'"""
        cur.execute(query)
        result = cur.fetchall()
        # this is a list with db records where each record is a tuple
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_lunch_recipes():
    db_connection = _connect_to_db()
    try:
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM recipes WHERE meal_type = 'lunch'"""
        cur.execute(query)
        result = cur.fetchall()
        # this is a list with db records where each record is a tuple
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_dinner_recipes():
    db_connection = _connect_to_db()
    try:
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM recipes WHERE meal_type = 'dinner'"""
        cur.execute(query)
        result = cur.fetchall()
        # this is a list with db records where each record is a tuple
        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def delete_recipe_by_id(id):
    db_connection = _connect_to_db()
    try:

        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM recipes WHERE recipe_id = {}""".format(id)
        cur.execute(del_query)

        db_connection.commit()
        print(f"Record with recipe_id {id} deleted successfully.")

        select_query = "SELECT * FROM recipes"
        cur.execute(select_query)
        remaining_recipes = cur.fetchall()  # Get all remaining records
        cur.close()

        return remaining_recipes

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

if __name__ == "__main__":
    get_all_recipe_collection()
    get_breakfast_recipes()
    get_lunch_recipes()
    get_dinner_recipes()
    get_all_recipe_with_id()