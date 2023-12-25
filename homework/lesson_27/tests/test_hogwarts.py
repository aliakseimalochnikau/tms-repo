"""
4. Написать тесты, которые:
- находят всех, родившихся в 1980м году
- найти, кто родился раньше всех
- добавляют волшебника со случайными данными и проверяют его наличие в базе. Потом можно его удалить
=== Со звёздочкой ===
- найти всех, кто не родился в 1980м году
- найти всех полукровок (полукровка - рожденный от магла ИЛИ от другого вида ;))
"""

from homework.lesson_27.data.data import Wizard, generate_wizard
from homework.lesson_27.database import TABLE_NAME

harry_potter = Wizard(first_name='Harry', last_name='Potter', blood_status='Half-blood', born=1980)
ronald_weasley = Wizard(first_name='Ronald', last_name='Weasley', blood_status='Pure-blood', born=1979)
hearmione_granger = Wizard(first_name='Hermione', last_name='Granger', blood_status='Muggle-born', born=1979)
neville_longbottom = Wizard(first_name='Neville', last_name='Longbottom', blood_status='Pure-blood', born=1980)
rubeus_hagrid = Wizard(first_name='Rubeus', last_name='Hagrid', blood_status='Half-breed', born=1928)


class TestHogwarts:
    def test_born_in_1980(self, db_connector):
        db = db_connector
        wizards = db.read_from_db(
            f"SELECT * from {TABLE_NAME} "
            f"WHERE born = 1980;"
        )
        expected_wizards = [harry_potter, neville_longbottom]
        assert expected_wizards == wizards, f"Expected {expected_wizards}, but got {wizards}"

    def test_oldest_wizard(self, db_connector):
        db = db_connector
        wizards = db.read_from_db(
            f"SELECT * from {TABLE_NAME} "
            f"WHERE born IN (SELECT MIN(born) from {TABLE_NAME});"
        )
        expected_wizards = [rubeus_hagrid]
        assert expected_wizards == wizards, f"Expected {expected_wizards}, but got {wizards}"

    def test_new_wizard_added(self, db_connector):
        db = db_connector
        wizard = generate_wizard()
        db.write_to_db(
            f"INSERT INTO {TABLE_NAME} "
            f"VALUES ('{wizard.first_name}', '{wizard.last_name}', '{wizard.blood_status}', {wizard.born});"
        )
        wizards = db.read_from_db(
            f"SELECT * from {TABLE_NAME};")
        assert wizard in wizards, f"Expected {wizard} to be in {wizards}, but wasn't found"

    def test_not_born_in_1980(self, db_connector):
        db = db_connector
        wizards = db.read_from_db(
            f"SELECT * from {TABLE_NAME} "
            f"WHERE born != 1980;"
        )
        expected_wizards = [ronald_weasley, hearmione_granger, rubeus_hagrid]
        assert expected_wizards == wizards, f"Expected {expected_wizards}, but got {wizards}"

    def test_not_pure_blood(self, db_connector):
        db = db_connector
        wizards = db.read_from_db(
            f"SELECT * from {TABLE_NAME} "
            f"WHERE blood_status != 'Pure-blood';"
        )
        expected_wizards = [harry_potter, hearmione_granger, rubeus_hagrid]
        assert expected_wizards == wizards, f"Expected {expected_wizards}, but got {wizards}"
