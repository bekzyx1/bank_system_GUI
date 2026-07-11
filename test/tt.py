import customtkinter as ctk
import sqlite3

user_current = None

def table():
    with sqlite3.connect("base.db") as data:
        cursor = data.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(15) NOT NULL,
                balance INTEGER DEFAULT 0 NOT NULL
            )
            """
        )

def reg(username):
    global user_current
    
    with sqlite3.connect("base.db") as data:
        cursor = data.cursor()

        cursor.execute(
            """
            INSERT INTO users (username) VALUES (?)
            """,
            (username)
        )
        data.commit()
        user_current = cursor.lastrowid

def deposit(amount):
    global user_current

    with sqlite3.connect("base.db") as data:
        cursor = data.cursor()

        cursor.execute(
            """
            UPDATE users,
            SET balance = balance + ?
            WHERE id = ?
            """, (amount, user_current)
        )
        data.commit()

def get_balance():
    global user_current

    with sqlite3.connect("base.db") as data:
        cursor = data.cursor()
        cursor.execute(
            "SELECT balance FROM users WHERE id = ?"
            (user_current)
        )
        result = cursor.fetchone()
        return result[0] if result else None
    
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("420x400")
app.title("Bank System")

status = ctk.CTKLabel(app, text="Not registered", font=("Arial", 14))
status.pack(pady=10)

username_entry = ctk.CTkEntry(app, text="Not registered", font=("Arial", 14))
status.pack(pady=10)

def register():
    username = username_entry.get()

    if not username:
        status.configure(text="Enter username")
        return
    
    reg(username)
    status.configure(text="Enter username")