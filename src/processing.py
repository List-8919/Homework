from datetime import datetime

def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Функция возвращает новый список словарей, содержащий
    только те словари, у которых ключ state.
    """

    filtered_data = [item for item in data if item.get('state', '').lower() == state.lower()]
    return filtered_data


def sort_by_date(items, descending=True):
    """
    Сортирует список словарей по ключу 'date'
    и возвращает новый, отсортированный списокпо дате.
    """
    sorted_items = sorted(items, key=lambda x: datetime.fromisoformat(x["date"]),reverse=descending)
    return sorted_items


if __name__ == "__main__":


    list_dicts = [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(list_dicts))
