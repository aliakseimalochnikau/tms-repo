import json


def read_file() -> list:
    with open("HW_files.txt", encoding="UTF-8") as file:
        characters = file.read().splitlines()
    return characters


def list_to_dict(lst: list) -> dict:
    temp = []
    characters = {}
    for el in lst:
        temp.append(el.split(','))
        characters.update({temp[0][0]: temp[0][1]})
        temp.clear()
    return characters


def write_json(contents: dict) -> None:
    with open("HarryPotter.json", "w", encoding="UTF-8") as file:
        json.dump(
            contents,
            file,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )


if __name__ == "__main__":
    chars_list = read_file()
    chars_dict = list_to_dict(chars_list)
    write_json(chars_dict)
