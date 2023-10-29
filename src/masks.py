import os


def get_card_mask(card: str) -> str:
    """
    Возвращает маску карты
    :param card: номер карты на входе
    :return: маска карты в формате xxxx xx** **** xxxx
    """
    symbols = []

    if len(card) != 16 or not card.isdigit():
        return "Неверно указана карта"

    for symbol in range(0, len(card), 4):
        symbols.append(card[symbol: symbol + 4])
    return f"{symbols[0]} {symbols[1][:2]}** **** {symbols[3]}"


def get_bank_account(bank_acc: str) -> str:
    """
    Возвращает маску банковского счета
    :param bank_acc: номер счета на входе
    :return: маска счета в видео ****xx
    """
    if not bank_acc.isdigit():
        return "Неверно указан счет"

    return f"**{bank_acc[-4:]}"


def count_files_and_folders(path=os.getcwd(), is_recursive=False):
    files = []
    folders = []
    if not is_recursive:
        list_of_files_and_dirs = os.listdir()
        for item in list_of_files_and_dirs:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                folders.append(item)
            else:
                files.append(item)
        return {"files": len(files), "folders": len(folders)}

    files_and_folders = os.walk(path)
    for item in files_and_folders:
        for folder in item[1]:
            folders.append(folder)
        for file in item[2]:
            files.append(file)
    return {"files": len(files), "folders": len(folders)}
