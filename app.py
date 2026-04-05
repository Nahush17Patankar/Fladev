

import time
import mysql.connector

for i in range(10):
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="testdb"
        )
        print("Connected to DB!")
        break
    except:
        print("Retrying DB connection...")
        time.sleep(5)
print("App finished successfully")
exit(0)