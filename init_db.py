import sqlite3

# Connect (or create) the database
conn = sqlite3.connect("convention.db")
c = conn.cursor()

# Create tables
c.executescript("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS conventions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT
);

CREATE TABLE IF NOT EXISTS interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS user_conventions (
    user_id INTEGER,
    convention_id INTEGER
);

CREATE TABLE IF NOT EXISTS user_interests (
    user_id INTEGER,
    interest_id INTEGER
);
""")

# Insert sample data
c.executescript("""
INSERT INTO users (name) VALUES ('Alex'), ('Jamie'), ('Chris');

INSERT INTO conventions (name, location) VALUES ('Anime Expo', 'Los Angeles');

INSERT INTO interests (name) VALUES ('Cosplay'), ('TCG'), ('Video Games');

INSERT INTO user_conventions VALUES (1,1),(2,1),(3,1);
INSERT INTO user_interests VALUES (1,1),(1,2),(2,1),(3,3);
""")

conn.commit()
conn.close()

print("Database created and populated successfully!")
