import sqlite3

DB = "bot.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, wallet TEXT, ref TEXT)")
        conn.commit()

def get_user(user_id):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return c.fetchone()

def save_user(user_id, wallet, ref):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        if not get_user(user_id):
            c.execute("INSERT INTO users (id, wallet, ref) VALUES (?, ?, ?)", (user_id, wallet, ref))
            conn.commit()

def get_ref_count(ref):
    with sqlite3.connect(DB) as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users WHERE ref=?", (str(ref),))
        return c.fetchone()[0]