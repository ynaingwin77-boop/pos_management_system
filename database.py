import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "pos.db")

def create_table():
    conn = sqlite3.connect(DB_PATH)
    try:
         with conn:
             conn.execute("""
                          CREATE TABLE IF NOT EXISTS CATEGORIES(
                              categor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                              is_deleted INTEGER DEFAULT 0,
                              category_name TEXT NOT NULL
                              
                          )
                          """)
             conn.execute("""
                          CREATE TABLE IF NOT EXISTS PRODUCTS(
                              product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                              product_name TEXT NOT NULL,
                              quantity INTEGER DEFAULT 0,
                              price REAL NOT NULL,
                              category_id INTEGER,
                              is_deleted INTEGER DEFAULT 0,
                              FOREIGN KEY (category_id) REFERENCES CATEGORIES(categor_id)
                          )
                          """)
    except sqlite3.Error as e:
         print("Database error:", e)
    finally:
         conn.close()
         