def get_list_by_key(input_list: list[dict], key="EXECUTED") -> list[dict]:
    """
    принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение
    :param input_list: список словарей
    :param key: значение для ключа state, по умолчанию == EXECUTED
    :return: список словарей по значению ключа state
    """
    new_list: list[dict] = []
    for element in input_list:
        if element['state'] == key:
            new_list.append(element)
    return new_list


def sort_by_date(input_list: list[dict], by_raise: bool = True) -> list[dict]:
    """
    принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты
    :param input_list: список словарей
    :param by_raise: сортируем по убыванию или по возрастанию, True = по убыванию
    :return: отсортированный по дате список словарей
    """
    return sorted(input_list, key=lambda element: element['date'], reverse=by_raise)


def sort_products(input_list: list[dict], category: str = "") -> list[dict]:
    """
    доп.задача 1
    Возвращает список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории. Если категория не задана,
    то сортировка производится для всех продуктов.
    :param input_list: список словарей
    :param category: категория продуктов, если не указана - не учитывается
    :return: отсортированный по цене список словарей
    """
    if category == "":
        return sorted(input_list, key=lambda product: product['price'], reverse=True)

    new_list: list[dict] = []
    for element in input_list:
        if element['category'].lower() == category.lower():
            new_list.append(element)
    return sorted(new_list, key=lambda product: product['price'], reverse=True)

