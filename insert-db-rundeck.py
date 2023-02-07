import psycopg2
import os

def import_sql(file_path):
    # Connect to the database
    conn = psycopg2.connect(
        host="host_name",
        database="database_name",
        user="user_name",
        password="password"
    )

    # Create a cursor
    cur = conn.cursor()

    # Open the SQL file and execute its commands
    with open(file_path, "r") as f:
        cur.execute(f.read())

    # Commit the changes
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()

# Get the path to the SQL file from the user
file_path = input("Enter the path to the SQL file:")

# Check if the file exists
if os.path.isfile(file_path):
    import_sql(file_path)
else:
    print("The file does not exist.")
