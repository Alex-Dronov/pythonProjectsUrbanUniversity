import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")
users = cursor.execute("SELECT id FROM Users")
if users.fetchone() is None:
    for i in range(1,11):
        # pass
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ? )",
                       (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

for user in cursor.execute("SELECT * FROM Users"):
    print(user)
print()

users = cursor.execute("SELECT id FROM Users")
if users.fetchone() is not None:
    for i in range(1,11,2):
        # pass
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",
                       ("500", f"{i}"))

for user in cursor.execute("SELECT * FROM Users"):
    print(user)
print()

users = cursor.execute("SELECT id FROM Users")
if users.fetchone() is not None:
    for i in range(1,11,3):
        cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

for user in cursor.execute("SELECT * FROM Users"):
    print(user)
print()

cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

connection.commit()
connection.close()