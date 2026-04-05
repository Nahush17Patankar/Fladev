

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

@app.route('/')
def home():
    return "Falsk is running with mysql"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)