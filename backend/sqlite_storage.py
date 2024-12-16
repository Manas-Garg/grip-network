import sqlite3

def save_to_db(data, table_name="climate_data"):
    """Save data into a local SQLite database."""
    conn = sqlite3.connect("climate_data.db")
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            timestamp TEXT,
            metric TEXT,
            value REAL
        )
    """)
    for entry in data:
        cursor.execute(f"""
            INSERT INTO {table_name} (timestamp, metric, value)
            VALUES (?, ?, ?)
        """, (entry['timestamp'], entry['metric'], entry['value']))
    conn.commit()
    conn.close()
    print(f"Data successfully saved to {table_name} in SQLite.")

if __name__ == "__main__":
    # Example data structure
    sample_data = [
        {"timestamp": "2024-12-14T00:00:00Z", "metric": "carbon", "value": 415.26},
        {"timestamp": "2024-12-14T01:00:00Z", "metric": "temperature", "value": 21.5},
    ]
    save_to_db(sample_data)
