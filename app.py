# from flask import Flask
# import mysql.connector

# app = Flask(__name__)

# @app.route('/')
# def home():
#     try:
#         db = mysql.connector.connect(
#             host="db",
#             user="root",
#             password="root",
#             database="testdb"
#         )
#         return "Connected to MySQL successfully!"
#     except:
#         return "Database connection failed!"

# if __name__ == "__main__":
#     app.run(host="localhost", port=5000)



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