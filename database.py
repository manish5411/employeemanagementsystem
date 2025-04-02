import pymysql
from tkinter import messagebox

# Establishing Connection Function
def connect_database():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='YASHITA1124', database='employee_data')
        mycursor = conn.cursor()
        return conn, mycursor
    except Exception as e:
        messagebox.showerror('Error', f'Something went wrong: {e}')
        return None, None

# Delete All Records
def delete_all():
    """Delete all records from the employee table."""
    conn, mycursor = connect_database()
    if conn is None:
        return

    try:
        mycursor.execute("DELETE FROM data")  # Ensure 'data' is your correct table name
        conn.commit()
        messagebox.showinfo('Success', 'All employees deleted successfully')
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to delete all records: {e}')
    finally:
        conn.close()

def phone_exists(phone):
    conn, mycursor = connect_database()
    if conn is None:
        return False

    try:
        mycursor.execute("SELECT COUNT(*) FROM data WHERE Phone = %s", (phone,))
        result = mycursor.fetchone()
        return result[0] > 0  # Returns True if phone exists
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to check phone number: {e}')
        return False
    finally:
        conn.close()


# Search Function
import pymysql
from tkinter import messagebox

def search(option, value):
    conn, mycursor = connect_database()
    if conn is None:
        return []

    try:
        query = "SELECT Id, Name, Phone, Gender, Role, Salary FROM data WHERE " + option + " = %s"
        mycursor.execute(query, (value,))  # Using parameterized query
        result = mycursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Search failed: {e}')
        return []
    finally:
        if conn:
            conn.close()  # Close connection only if it was successfully opened



# Insert Data Function
def insert(id, name, phone, role, gender, salary):
    conn, mycursor = connect_database()
    if conn is None:
        return

    try:
        if id_exists(id):
            messagebox.showerror('Error', 'ID already exists')
            return

        if phone_exists(phone):  # Check for duplicate phone numbers
            messagebox.showerror('Error', 'Phone number already exists')
            return

        query = "INSERT INTO data (Id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id, name, phone, role, gender, salary)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo('Success', 'Data inserted successfully')

    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to insert data: {e}')
    finally:
        conn.close()

# Check If ID Exists
def id_exists(id):
    conn, mycursor = connect_database()
    if conn is None:
        return False

    try:
        mycursor.execute('SELECT COUNT(*) FROM data WHERE Id=%s', (id,))
        result = mycursor.fetchone()
        return result[0] > 0
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to check ID: {e}')
        return False
    finally:
        conn.close()

# Fetch Employee Data
def fetch_employee():
    conn, mycursor = connect_database()
    if conn is None:
        return []

    try:
        query = "SELECT Id, Name, Phone, Gender, Role, Salary FROM data"
        mycursor.execute(query)
        employees = mycursor.fetchall()
        return employees
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to fetch employees: {e}')
        return []
    finally:
        conn.close()



# Update Employee Data
def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    conn, mycursor = connect_database()
    if conn is None:
        return

    try:
        query = '''UPDATE data 
                   SET Name=%s, Phone=%s, Role=%s, Gender=%s, Salary=%s 
                   WHERE id=%s'''
        values = (new_name, new_phone, new_role, new_gender, new_salary, id)
        mycursor.execute(query, values)


        conn.commit()
        messagebox.showinfo('Success', 'Employee details updated successfully')
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to update data: {e}')
    finally:
        conn.close()


# Delete Employee Data
def delete(id):
    conn, mycursor = connect_database()
    if conn is None:
        return

    try:
        query = 'DELETE FROM data WHERE Id=%s'
        mycursor.execute(query, (id,))
        conn.commit()
        messagebox.showinfo('Success', 'Employee deleted successfully')
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to delete employee: {e}')
    finally:
        conn.close()

# Delete All Records
def deleteall_records():
    conn, mycursor = connect_database()
    if conn is None:
        return

    try:
        mycursor.execute('TRUNCATE TABLE data')
        conn.commit()
        messagebox.showinfo('Success', 'All records deleted successfully')
    except pymysql.MySQLError as e:
        messagebox.showerror('Error', f'Failed to delete all records: {e}')
    finally:
        conn.close()
