from flask import Flask, jsonify
from flask_cors import CORS
import random
import os
import logging
import mysql.connector

# -----------------------------
# Logging Setup
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


# -----------------------------
# User Functions
# -----------------------------

def get_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_table():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mood VARCHAR(50),
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()
    cursor.close()
    db.close()
    print("Table 'entries' created (or already exists).")

def insert_dummy_data():
    db = get_db()
    cursor = db.cursor()

    dummy_entries = [
        ("happy", "First test entry"),
        ("tired", "Long day at work"),
        ("excited", "Building my first full-stack app!"),
    ]

    cursor.executemany(
        "INSERT INTO entries (mood, note) VALUES (%s, %s)",
        dummy_entries
    )

    db.commit()
    cursor.close()
    db.close()
    print("Dummy data inserted.")

# -----------------------------
# Environment Variable Retrieval
# -----------------------------
DB_PASSWORD = os.environ.get("DB_PASSWORD")

if DB_PASSWORD is None:
    logger.warning("DB_PASSWORD environment variable is NOT set.")
else:
    logger.info("DB_PASSWORD environment variable successfully retrieved.")

DB_HOST = "democracy1434.mysql.pythonanywhere-services.com" 
DB_USER = "democracy1434" 
DB_NAME = "democracy1434$default"

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)
CORS(app, origins=[
    "http://127.0.0.1:5500",
    "https://michischwarz.github.io"
])

@app.get("/")
def home():
    logger.info("Home endpoint accessed.")
    return "Backend is running!"

@app.get("/api/random")
def random_number():
    number = random.randint(0, 100)
    logger.debug(f"Generated random number: {number}")
    return jsonify({"number": number})

@app.get("/api/entries")
def get_entries():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, mood, note, created_at
        FROM entries
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(rows)

@app.get("/api/reset_db")
def reset_db():
    logger.info("Reseting data base.")
    create_table()
    insert_dummy_data()
    return "Database has been reset."

if __name__ == "__main__":
    logger.info("Starting Flask server...")
    app.run(debug=True)
