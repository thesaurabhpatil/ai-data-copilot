import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE sales (
    id INTEGER,
    revenue INTEGER,
    date TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO sales VALUES (1, 1000, '2026-03-15')")
cursor.execute("INSERT INTO sales VALUES (2, 2000, '2026-03-16')")
cursor.execute("INSERT INTO sales VALUES (3, 1500, '2026-03-17')")

conn.commit()
conn.close()

print("Database created successfully ✅")