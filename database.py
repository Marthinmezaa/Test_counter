import sqlite3

# ----------------------
# Data base
# ----------------------
def create_database():
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_number TEXT,
            test_type TEXT,
            company TEXT,
            date TEXT,
            subjects INTEGER           
        )
    """)
    
    connection.commit()
    connection.close()

# ----------------------
# Insert test
# ----------------------
def insert_test(file_number, test_type, company, date, subjects):
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tests (file_number, test_type, company, date, subjects)
        VALUES (?, ?, ?, ?, ?)
    """, (file_number, test_type, company, date, subjects))

    connection.commit()
    connection.close()

# ----------------------
# Get test
# ----------------------
def get_all_test():
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tests")
    results = cursor.fetchall()

    connection.close()
    return results