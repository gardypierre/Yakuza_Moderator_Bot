import sqlite3
import os
from config import DB_NAME

DB_FILE = f"{DB_NAME}.db"

def get_db_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Table for user interactions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            interaction_type TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table for groups
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER NOT NULL UNIQUE,
            group_name TEXT,
            added_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

def log_interaction(user_id, username, first_name, last_name, interaction_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_interactions (user_id, username, first_name, last_name, interaction_type)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, username, first_name, last_name, interaction_type))
    conn.commit()
    conn.close()

def add_group(group_id, group_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO groups (group_id, group_name)
        VALUES (?, ?)
    """, (group_id, group_name))
    conn.commit()
    conn.close()

def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Count unique users
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM user_interactions")
    unique_users = cursor.fetchone()[0]

    # Count total interactions
    cursor.execute("SELECT COUNT(*) FROM user_interactions")
    total_interactions = cursor.fetchone()[0]

    # Count groups
    cursor.execute("SELECT COUNT(*) FROM groups")
    total_groups = cursor.fetchone()[0]

    conn.close()
    return unique_users, total_interactions, total_groups
