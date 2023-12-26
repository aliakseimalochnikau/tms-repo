import pytest
from homework.lesson_27.database import DataBase, TABLE_NAME


@pytest.fixture()
def db_connector():
    db = DataBase()
    db.create_table()
    db.write_to_db(
        f"INSERT INTO {TABLE_NAME} "
        f"VALUES "
        f"('Harry', 'Potter', 'Half-blood', 1980),"
        f"('Ronald', 'Weasley', 'Pure-blood', 1979),"
        f"('Hermione', 'Granger', 'Muggle-born', 1979),"
        f"('Neville', 'Longbottom', 'Pure-blood', 1980),"
        f"('Rubeus', 'Hagrid', 'Half-breed', 1928);"
    )
    yield db
    db.drop_table()
    db.connection.close()
