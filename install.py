import sqlite3
import os
import secrets

if not os.path.exists("database.db"):
    db = sqlite3.connect("database.db")

    database_cursor = db.cursor()


    try:
        with open("schema.sql", "r") as schema:
            schema_file = schema.read()

            database_cursor.executescript(schema_file)

            db.commit()
            db.close()
    except Exception as e:
        print(f"Error creating database.db: {e}")

    try:
        with open("config.py", "w") as config_file:
            secret_key = secrets.token_hex(32)
            config_file.write(f"SECRET_KEY = \"{secret_key}\"\n")
    except Exception as e:
        print(f"Error creating config.py: {e}")