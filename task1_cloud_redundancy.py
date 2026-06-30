import sqlite3

def init_db():
    conn = sqlite3.connect("cloud_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            department TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(name, email, department):
    conn = sqlite3.connect("cloud_data.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        print(f"[-] Error: Data injection rejected. Email '{email}' already exists in the system!")
        conn.close()
        return False
    else:
        cursor.execute("""
            INSERT INTO users (name, email, department) 
            VALUES (?, ?, ?)
        """, (name, email, department))
        conn.commit()
        print(f"[+] Success: Unique data verified and added for {name}.")
        conn.close()
        return True

if __name__ == "__main__":
    init_db()
    print("--- Cloud Database Redundancy Check System ---\n")
    
    add_user("Ahmed", "ahmed@sphinx.edu", "Computer Science")
    add_user("Sara", "sara@sphinx.edu", "Cybersecurity")
    
    print("\n--- Trying to insert duplicate data ---")
    add_user("Maged", "ahmed@sphinx.edu", "Information Technology")

