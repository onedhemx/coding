cities_list = []

def add_city(city):
    cities_list.append(city)

def sort_cities():
    return sorted(cities_list, key=len)

def remove_city(city):
    if city in cities_list:
        cities_list.remove(city)


cities_set = set()

def add_city(city):
    cities_set.add(city)

def sort_cities():
    return sorted(cities_set, key=len)

def remove_city(city):
    if city in cities_set:
        cities_set.remove(city)


cities_dict = {}

def add_city(city):
    cities_dict[city] = len(city)

def sort_cities():
    # сортируем по длине названия (значение)
    return sorted(cities_dict.items(), key=lambda item: item[1])

def remove_city(city):
    if city in cities_dict:
        del cities_dict[city]


cities_tuple = ()

def add_city(city):
    global cities_tuple
    cities_tuple = (*cities_tuple, city)

def sort_cities():
    return sorted(cities_tuple, key=len)

def remove_city(city):
    global cities_tuple
    cities_tuple = tuple(c for c in cities_tuple if c != city)
