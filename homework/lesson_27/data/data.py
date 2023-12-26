from dataclasses import dataclass
import random


@dataclass
class Wizard:
    first_name: str
    last_name: str
    blood_status: str
    born: int


def generate_wizard():
    return Wizard(
        first_name=random.choice(['James', 'Bill', 'Kate', 'Hanna']),
        last_name=random.choice(['Smith', 'Wells', 'Graham', 'White']),
        blood_status=random.choice(['Half-blood', 'Pure-blood', 'Muggle-born', 'Half-breed']),
        born=random.randint(1900, 1999)
    )
