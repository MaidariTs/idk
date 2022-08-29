"""Основы работы с SQLite."""
import sqlite3
from config import DATABASE


try:
    # Create a database connection
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Создаем пользователя с user_id = 1000
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (1234,))

    # Считываем всех пользователей
    users = cursor.execute("SELECT * FROM users")
    print(users.fetchall())

    # Подтверждаем изменения
    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if conn:
        conn.close()
