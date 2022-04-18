########################################
#   Обробка та видання даних клієнту   #
########################################

from getting.get_data_from_txt import get_data_from_txt


def json_data():
    acc_datas = get_data_from_txt()  # отримання даних з txt

    # print(acc_datas)
    return acc_datas
