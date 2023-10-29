from masks import get_card_mask, get_bank_account


def get_card_type_and_mask(card: str) -> str:
    """
    Возвращает маску карты с типом карты
    :param card: данные карты в виде строки типа "Visa Platinum xxxxxxxxxxxxxxxx"
    :return: данные карты в виде строки типа "Visa Platinum xxxx xx** **** xxxx"
    """
    card_info_list = card.split(" ")
    if "Счет" in card_info_list:
        return f"Счет {get_bank_account(card_info_list[-1])}"
    else:
        card_info_list[-1] = get_card_mask(card_info_list[-1])
        return " ".join(card_info_list)


def get_date(date: str) -> str:
    """
    Возвращает дату в формате dd.mm.yy
    :param date: строка, например "2018-07-11T02:26:18.671407"
    :return: дата, например "11.07.2018"
    """
    date_list = date.split("-")
    return f"{date_list[2][:2]}.{date_list[1]}.{date_list[0]}"


def extra_task_1(input_list: list[str]) -> list[str]:
    """
    Просто доп. задача
    :param input_list: список строк
    :return: список строк из элементов с одинаковыми первыми и последними буквами
    """
    output_list: list[str] = []

    if len(input_list) == 0:
        return output_list

    for element in input_list:
        if element[0] == element[-1]:
            output_list.append(element)

    return output_list


def extra_task_2(input_list: list[int]) -> int:
    """
    Просто вторая доп.задача
    :param input_list: целочисленный список
    :return: максимальное произведение двух чисел списка
    """
    if len(input_list) < 2:
        return 0
    max_multiply = input_list[0] * input_list[1]
    for i in range(len(input_list) - 1):
        if input_list[i] * input_list[i + 1] > max_multiply:
            max_multiply = input_list[i] * input_list[i + 1]
    return max_multiply
