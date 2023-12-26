"""
С использованием библиотеки sqlite3 выполнить следующее
1. Создать базу данных, в которой есть таблица Gryffindor
2. В таблице есть столбцы first_name, last_name, blood_status, born. Все имеют тип text, кроме последнего - int
3. Заполнить данными
Harry Potter Half-blood 1980
Ronald Weasley Pure-blood 1979
Hermione Granger Muggle-born 1979
Neville Longbottom Pure-blood 1980
Rubeus Hagrid Half-breed 1928
"""

import sqlite3
from homework.lesson_27.data.data import Wizard

DB_NAME = "Hogwarts.db"
TABLE_NAME = "Gryffindor"


class DataBase:

    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute(
            f"CREATE TABLE {TABLE_NAME} ("
            "first_name text, "
            "last_name text, "
            "blood_status text, "
            "born int);"
        )
        self.connection.commit()

    def drop_table(self):
        self.cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME};")
        self.connection.commit()

    def write_to_db(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def read_from_db(self, sql_query):
        rows = self.cursor.execute(sql_query).fetchall()
        wizards = [Wizard(*row) for row in rows]
        return wizards

