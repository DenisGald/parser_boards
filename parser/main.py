import requests

from config import LIMIT
from exporter import export_to_excel, export_to_json
from loader import fetch_map_data
from parser_module import parse_objects


def main():
    print("Загрузка данных с boards.by...")
    session = requests.Session()
    raw_data = fetch_map_data(session)

    print("Парсинг данных...")
    parsed_data = parse_objects(raw_data, LIMIT)
    print(f"Собрано сторон: {len(parsed_data)}")

    export_to_json(parsed_data)
    export_to_excel(parsed_data)
    print("Готово. Файлы result.json и result.xlsx созданы.")


if __name__ == "__main__":
    main()
