from faker import Faker
from homework.lesson_26.data import Person

Faker.seed()
fake = Faker('en-US')


def generated_data():
    yield Person(
        username=fake.user_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        password=fake.password(),
        phone_number=fake.phone_number(),
    )
