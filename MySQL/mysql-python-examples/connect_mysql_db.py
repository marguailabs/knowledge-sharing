#import mysql.connector
from mysql.connector import connect
from mysql.connector import Error

def connect_mysql():
    """Connect to MySQL database"""
    try:
        #connect()
        conn = connect(
            host="localhost",       # Change if using remote MySQL server
            user="root",            # Your MySQL username
            password="marguai", # Replace with your MySQL root password
            database="schooldb"     # Database we created
        )
        if conn.is_connected():
            print("✅ Connected to MySQL")
            return conn
    except Error as e:
        print(f"❌ Error: {e}")
        return None
    
def insert_data(conn):
    """Insert sample data into students"""
    try:
        cursor = conn.cursor()
        print(type(cursor))
        print(cursor)

        query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        values = [
            ("Alice", 20, "A"),
            ("Bob", 21, "B"),
            ("Charlie", 22, "A"),
        ]

        cursor.executemany(query, values)

        conn.commit()
        print(f"✅ Inserted {cursor.rowcount} rows")
    except Error as e:
        print(f"❌ Error inserting data: {e}")


def insert_one_data(conn):
    """Insert sample data into students"""
    try:
        cursor = conn.cursor()
        print(type(cursor))
        print(cursor)

        query = "INSERT INTO students (name, age, grade) VALUES ('Alice', 20, 'A')"
        
        cursor.execute(query)
        
        conn.commit()
        print(f"✅ Inserted {cursor.rowcount} rows")
    except Error as e:
        print(f"❌ Error inserting data: {e}")   


def fetch_data(conn):
    """Fetch and display student records"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()
        print("\n📊 Student Records:")

        for row in rows:
            print(row)
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print("\n")
    except Error as e:
        print(f"❌ Error fetching data: {e}")

# list, tuple, set, dictionary


if __name__ == "__main__":
    message = "Hello Friends!"
    print(message)

    conn_obj = connect_mysql()
    print(conn_obj)

    #insert_one_data(conn_obj)
    fetch_data(conn_obj)