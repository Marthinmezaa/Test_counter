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

# ----------------------
# Get test by file number
# ----------------------
def get_test_by_file_number(file_number):
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test WHERE file_number=?', (file_number,))
    results = cursor.fetchall()
    connection.close()
    return results

# ----------------------
# Delete test by ID
# ----------------------
def delete_test(test_id):
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM test WHERE id=?', (test_id,))
    connection.commit()
    delete_rows = cursor.rowcount
    connection.close()
    return delete_rows

# ----------------------
# Update test by ID
# ----------------------
def update_test(test_id, file_number, test_type, company, date, subjects):
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE test
        SET file_number=?, test_type=?, company=?, date=?, subjects=?
        WHERE id=?
    ''', (file_number, test_type, company, date, subjects, test_id))

    connection.commit()
    update_rows = cursor.rowcount
    connection.close()
    return update_rows

# ----------------------
# Get test by ID
# ----------------------
def get_test_by_id(test_id):
    connection = sqlite3.connect('tests.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test WHERE id=?', (test_id,))
    result = cursor.fetchone()
    connection.close()
    return result