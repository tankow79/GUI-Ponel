#############################################
#   Отримання даних з txt віддавання json   #
#############################################


def get_acc_data_acc_txt():
    """отримати acc pas:log з acc.txt і повернути список"""

    acc_data_lists = []
    with open('acc.txt', 'r', encoding='utf-8') as input_file:
        input_data1 = input_file.read().split('\n')
        input_data = list(filter(None, input_data1))
        for line in input_data:
            try:
                splitted_line = line.split(':')
                if splitted_line == ['', '']:
                    return None
                acc_data = [splitted_line[0], splitted_line[1]]
                acc_data_lists.append(acc_data)
            except IndexError:
                return None

    # перевірка отриманих даних
    if not acc_data_lists:
        return None

    return acc_data_lists


def conversion_list_to_json(acc_datas):
    """  перетворення списку в json формат """

    acc_data = []

    for acc_data_i in acc_datas:
        acc_data.append(
            {
                'login': acc_data_i[0],
                'password': acc_data_i[1]
            }
        )

    return acc_data


def get_data_from_txt():
    acc_datas = get_acc_data_acc_txt()  # читаю текстовик і повертаю список з данними акаунтів

    acc_datas_json = conversion_list_to_json(acc_datas)  # задаю зписку json формат

    return acc_datas_json
