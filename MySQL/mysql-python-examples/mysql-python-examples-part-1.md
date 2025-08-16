# MySQL Python Examples

Great 👍 thanks for sharing the MySQL version — since you’re on **MySQL 8.0.43** in Ubuntu, we’ll use the **official connector** (`mysql-connector-python`). I’ll walk you through the **full steps** with a working code example.

---

# 🔹 Steps to Connect Python with MySQL 8 on Ubuntu

### 1. ✅ Install Required Packages

Make sure you have the connector installed:

```bash
pip install mysql-connector-python
```

If you don’t have `pip`, install it:

```bash
sudo apt update
sudo apt install python3-pip -y
```

---

### 2. ✅ Start MySQL and Create Database

Start MySQL service:

```bash
sudo systemctl start mysql
```

Login to MySQL:

```bash
mysql -u root -p
```

Inside MySQL shell:

```sql
-- Create database
CREATE DATABASE schooldb;

-- Use the database
USE schooldb;

-- Create a sample table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10)
);
```

---

### 3. ✅ Python Program Example

Below is a complete Python program that:

1. Connects to MySQL
2. Creates the table if not exists
3. Inserts sample records
4. Fetches and prints results

```python
import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Connect to MySQL database"""
    try:
        conn = mysql.connector.connect(
            host="localhost",       # Change if using remote MySQL server
            user="root",            # Your MySQL username
            password="your_password", # Replace with your MySQL root password
            database="schooldb"     # Database we created
        )
        if conn.is_connected():
            print("✅ Connected to MySQL")
            return conn
    except Error as e:
        print(f"❌ Error: {e}")
        return None


def create_table(conn):
    """Create students table"""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                grade VARCHAR(10)
            )
        """)
        conn.commit()
        print("✅ Table created (if not exists)")
    except Error as e:
        print(f"❌ Error creating table: {e}")


def insert_data(conn):
    """Insert sample data into students"""
    try:
        cursor = conn.cursor()
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


def fetch_data(conn):
    """Fetch and display student records"""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("\n📊 Student Records:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"❌ Error fetching data: {e}")


if __name__ == "__main__":
    conn = connect_mysql()
    if conn:
        create_table(conn)
        insert_data(conn)
        fetch_data(conn)
        conn.close()
```

---

### 4. ✅ Expected Output

When you run the program:

```
✅ Connected to MySQL
✅ Table created (if not exists)
✅ Inserted 3 rows

📊 Student Records:
(1, 'Alice', 20, 'A')
(2, 'Bob', 21, 'B')
(3, 'Charlie', 22, 'A')
```

---

## 🔹 Summary

* Install MySQL + Python connector
* Create database + table
* Run Python script to insert and fetch data

---
