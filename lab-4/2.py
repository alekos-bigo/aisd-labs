from collections import deque

stations = [
    {'index': 0, 'branch': 'Кировско-Выборгская линия', 'station': 'Девяткино'},
    {'index': 1, 'branch': 'Кировско-Выборгская линия', 'station': 'Гражданский проспект'},
    {'index': 2, 'branch': 'Кировско-Выборгская линия', 'station': 'Академическая'},
    {'index': 3, 'branch': 'Кировско-Выборгская линия', 'station': 'Политехническая'},
    {'index': 4, 'branch': 'Кировско-Выборгская линия', 'station': 'Площадь Мужества'},
    {'index': 5, 'branch': 'Кировско-Выборгская линия', 'station': 'Лесная'},
    {'index': 6, 'branch': 'Кировско-Выборгская линия', 'station': 'Выборгская'},
    {'index': 7, 'branch': 'Кировско-Выборгская линия', 'station': 'Площадь Ленина'},
    {'index': 8, 'branch': 'Кировско-Выборгская линия', 'station': 'Чернышевская'},
    {'index': 9, 'branch': 'Кировско-Выборгская линия', 'station': 'Площадь Восстания'},
    {'index': 10, 'branch': 'Кировско-Выборгская линия', 'station': 'Владимирская'},
    {'index': 11, 'branch': 'Кировско-Выборгская линия', 'station': 'Пушкинская'},
    {'index': 12, 'branch': 'Кировско-Выборгская линия', 'station': 'Технологический институт 1'},
    {'index': 13, 'branch': 'Кировско-Выборгская линия', 'station': 'Балтийская'},
    {'index': 14, 'branch': 'Кировско-Выборгская линия', 'station': 'Нарвская'},
    {'index': 15, 'branch': 'Кировско-Выборгская линия', 'station': 'Кировский завод'},
    {'index': 16, 'branch': 'Кировско-Выборгская линия', 'station': 'Автово'},
    {'index': 17, 'branch': 'Кировско-Выборгская линия', 'station': 'Ленинский проспект'},
    {'index': 18, 'branch': 'Кировско-Выборгская линия', 'station': 'Проспект Ветеранов'},
    {'index': 19, 'branch': 'Московско-Петроградская линия', 'station': 'Парнас'},
    {'index': 20, 'branch': 'Московско-Петроградская линия', 'station': 'Проспект Просвещения'},
    {'index': 21, 'branch': 'Московско-Петроградская линия', 'station': 'Озерки'},
    {'index': 22, 'branch': 'Московско-Петроградская линия', 'station': 'Удельная'},
    {'index': 23, 'branch': 'Московско-Петроградская линия', 'station': 'Пионерская'},
    {'index': 24, 'branch': 'Московско-Петроградская линия', 'station': 'Чёрная речка'},
    {'index': 25, 'branch': 'Московско-Петроградская линия', 'station': 'Петроградская'},
    {'index': 26, 'branch': 'Московско-Петроградская линия', 'station': 'Горьковская'},
    {'index': 27, 'branch': 'Московско-Петроградская линия', 'station': 'Невский проспект'},
    {'index': 28, 'branch': 'Московско-Петроградская линия', 'station': 'Сенная площадь'},
    {'index': 29, 'branch': 'Московско-Петроградская линия', 'station': 'Технологический институт 2'},
    {'index': 30, 'branch': 'Московско-Петроградская линия', 'station': 'Фрунзенская'},
    {'index': 31, 'branch': 'Московско-Петроградская линия', 'station': 'Московские ворота'},
    {'index': 32, 'branch': 'Московско-Петроградская линия', 'station': 'Электросила'},
    {'index': 33, 'branch': 'Московско-Петроградская линия', 'station': 'Парк Победы'},
    {'index': 34, 'branch': 'Московско-Петроградская линия', 'station': 'Московская'},
    {'index': 35, 'branch': 'Московско-Петроградская линия', 'station': 'Звёздная'},
    {'index': 36, 'branch': 'Московско-Петроградская линия', 'station': 'Купчино'},
    {'index': 37, 'branch': 'Невско-Василеостровская линия', 'station': 'Беговая'},
    {'index': 38, 'branch': 'Невско-Василеостровская линия', 'station': 'Зенит'},
    {'index': 39, 'branch': 'Невско-Василеостровская линия', 'station': 'Приморская'},
    {'index': 40, 'branch': 'Невско-Василеостровская линия', 'station': 'Василеостровская'},
    {'index': 41, 'branch': 'Невско-Василеостровская линия', 'station': 'Гостиный двор'},
    {'index': 42, 'branch': 'Невско-Василеостровская линия', 'station': 'Маяковская'},
    {'index': 43, 'branch': 'Невско-Василеостровская линия', 'station': 'Площадь Александра Невского 1'},
    {'index': 44, 'branch': 'Невско-Василеостровская линия', 'station': 'Елизаровская'},
    {'index': 45, 'branch': 'Невско-Василеостровская линия', 'station': 'Ломоносовская'},
    {'index': 46, 'branch': 'Невско-Василеостровская линия', 'station': 'Пролетарская'},
    {'index': 47, 'branch': 'Невско-Василеостровская линия', 'station': 'Обухово'},
    {'index': 48, 'branch': 'Невско-Василеостровская линия', 'station': 'Рыбацкое'},
    {'index': 49, 'branch': 'Правобережная линия', 'station': 'Спасская'},
    {'index': 50, 'branch': 'Правобережная линия', 'station': 'Достоевская'},
    {'index': 51, 'branch': 'Правобережная линия', 'station': 'Лиговский проспект'},
    {'index': 52, 'branch': 'Правобережная линия', 'station': 'Площадь Александра Невского 2'},
    {'index': 53, 'branch': 'Правобережная линия', 'station': 'Новочеркасская'},
    {'index': 54, 'branch': 'Правобережная линия', 'station': 'Ладожская'},
    {'index': 55, 'branch': 'Правобережная линия', 'station': 'Проспект Большевиков'},
    {'index': 56, 'branch': 'Правобережная линия', 'station': 'Улица Дыбенко'},
    {'index': 57, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Комендантский проспект'},
    {'index': 58, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Старая Деревня'},
    {'index': 59, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Крестовский остров'},
    {'index': 60, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Чкаловская'},
    {'index': 61, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Спортивная'},
    {'index': 62, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Адмиралтейская'},
    {'index': 63, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Садовая'},
    {'index': 64, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Звенигородская'},
    {'index': 65, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Обводный канал'},
    {'index': 66, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Волковская'},
    {'index': 67, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Бухарестская'},
    {'index': 68, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Международная'},
    {'index': 69, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Проспект Славы'},
    {'index': 70, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Дунайская'},
    {'index': 71, 'branch': 'Фрунзенско-Приморская линия', 'station': 'Шушары'}
]


def get_data():
    start = input('Введите станцию отправления: ')
    end = input('Введите станцию прибытия: ')

    return start, end


def get_graph():
    graph = [[] for _ in range(len(stations))]

    # Красная ветка переходы
    graph[9].append(42)
    graph[10].append(50)
    graph[11].append(64)
    graph[12].append(29)

    # Синяя ветка переходы
    graph[27].append(41)
    graph[28].append(63)
    graph[28].append(49)
    graph[29].append(12)

    # Зеленая ветка переходы
    graph[41].append(27)
    graph[42].append(9)
    graph[43].append(52)

    # Оранжевая ветка переходы
    graph[49].append(28)
    graph[49].append(63)
    graph[50].append(10)
    graph[52].append(43)

    # Фиолетовая ветка переходы
    graph[63].append(49)
    graph[63].append(28)
    graph[64].append(11)

    for i in range(1, len(stations)):
        if stations[i]['branch'] == stations[i - 1]['branch']:
            graph[i].append(stations[i - 1]['index']) if stations[i - 1]['index'] not in graph[i] else None
            graph[i - 1].append(stations[i]['index']) if stations[i]['index'] not in graph[i - 1] else None

    return graph


def search_index_for_stations(start, end):
    for station in stations:
        if station['station'] == start:
            start = station['index']
        if station['station'] == end:
            end = station['index']

    return start, end


def bfs_shorter_path(graph, start, end):
    queue = deque()
    queue.append((start, [start]))  # Очередь содержит кортежи (узел, путь до этого узла)
    visited = set()  # Множество для отслеживания посещенных узлов

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == end:
                    return path + [neighbor]  # Найден кратчайший путь до конечного узла
                else:
                    queue.append((neighbor, path + [neighbor]))


def dfs_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return path

    shortest_path = None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_shortest_path(graph, neighbor, end, path)
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path

    return shortest_path


def decode_path(path):
    final_path = []

    for index in path:
        for station in stations:
            if station['index'] == index:
                final_path.append(station['station'])
                break

    return final_path


def main():
    graph = get_graph()
    start, end = get_data()
    start, end = search_index_for_stations(start, end)
    shorter_path_1 = bfs_shorter_path(graph, start, end)
    shorter_path_2 = dfs_shortest_path(graph, start, end)
    print(f"\nПри обходе в ширину:\nКоличество станций: {len(shorter_path_1)}\n{' -> '.join(decode_path(shorter_path_1))}\n")
    print(f"При обходе в глубину:\nКоличество станций: {len(shorter_path_2)}\n{' -> '.join(decode_path(shorter_path_2))}")


if __name__ == '__main__':
    main()
