import psycopg2
import csv

def get_connection():
    return psycopg2.connect(
        dbname="phonebook_db2",
        user="postgres",
        password="loaded12345",
        host="localhost",
        port="5432"
    )

def insert_from_csv(file_path):
    conn = get_connection()
    cur = conn.cursor()
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                try:
                    cur.execute("CALL insert_or_update_user(%s, %s)", (row[0], row[1]))
                except Exception as e:
                    print(f"Error inserting {row}: {e}")
    conn.commit()
    cur.close()
    conn.close()

# input by console
def insert_or_update_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
        conn.commit()
        print("Inserted or updated.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# insert many by console
def insert_many():
    names = [n.strip() for n in input("Enter names separated by comma: ").split(',')]
    phones = [p.strip() for p in input("Enter phones separated by comma: ").split(',')]
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT insert_many_users(%s, %s)", (names, phones))
        result = cur.fetchone()
        print("Invalid entries:", result[0])
        conn.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# search by pattern (phone num or name)
def search_pattern():
    pattern = input("Enter pattern to search (name or phone part): ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# pagination (show table from to)
def paginate():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM get_paginated_phonebook(%s, %s)", (limit, offset))
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# deletion of member
def delete_proc():
    value = input("Enter name or phone to delete: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_user(%s)", (value,))
        conn.commit()
        print("Deleted.")
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# querying data by name or phone num
def query_data():
    field = input("Filter by (1) Name or (2) Phone? Enter 1 or 2: ")
    value = input("Enter filter value: ")
    conn = get_connection()
    cur = conn.cursor()
    try:
        if field == "1":
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{value}%",))
        elif field == "2":
            cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", (f"%{value}%",))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# sort by name or phone num
def sort_table():
    sort_by = input("Sort by (first_name or phone): ").strip()
    direction = input("Direction (asc or desc): ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM get_sorted_phonebook(%s, %s)", (sort_by, direction))
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

def init_procedures():
    conn = get_connection()
    cur = conn.cursor()
    # SQL to create procedures and functions goes here (omitted for now)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    create_table()
    init_procedures()
    print("PhoneBook Ready.")
    while True:
        print("""
Choose an action:
1. Insert from CSV file 
2. Insert/Update single user 
3. Insert many users 
4. Search by pattern 
5. Paginate records 
6. Delete by name or phone 
7. Querying data
8. Sort records 
9. Exit
        """)
        choice = input("Enter choice (1-9): ")
        if choice == "1":
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_or_update_console()
        elif choice == "3":
            insert_many()
        elif choice == "4":
            search_pattern()
        elif choice == "5":
            paginate()
        elif choice == "6":
            delete_proc()
        elif choice == "7":
            query_data()
        elif choice == "8":
            sort_table()
        elif choice == "9":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again.")
