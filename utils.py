import json

"""Загружает данные из файла"""


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


"""Показывает всех кандидатов"""


def get_oll():
    return load_candidates()


"""Возвращает кандидата по pk"""


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return 'Not Found'


"""Возвращает кандидата по имени"""


def get_by_name(username):
    result = []
    for candidate in load_candidates():
        if username.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


"""Возвращает кандидатов по навыку"""


def get_by_skill(skill):
    result = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
