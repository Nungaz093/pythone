# import sqlite3
#
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS students(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         surname TEXT NOT NULL,
#         name TEXT NOT NULL,
#         patronymic TEXT NOT NULL,
#         age INTEGER NOT NULL CHECK (age >= 16 AND age <= 45)
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS courses(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course TEXT NOT NULL
#     )""")
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS registration(
#         ID_st INTEGER NOT NULL,
#         ID_c INTEGER NOT NULL,
#         FOREIGN KEY (ID_st) REFERENCES students(id)
#         FOREIGN KEY (ID_c) REFERENCES courses(id)
#     )""")
