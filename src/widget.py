import masks


def get_card_type_and_mask(card: str) -> str:
    """
    Возвращает маску карты с типом карты
    :param card: данные карты в виде строки типа "Visa Platinum xxxxxxxxxxxxxxxx"
    :return: данные карты в виде строки типа "Visa Platinum xxxx xx** **** xxxx"
    """
    card_info_list = card.split(" ")
    if "Счет" in card_info_list:
        return f"Счет **{card[-4:]}"
    else:
        card_info_list[-1] = masks.get_card_mask(card_info_list[-1])
        return " ".join(card_info_list)


