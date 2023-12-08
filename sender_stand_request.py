import configuration
import requests


# Создание нового заказа
def post_new_order(new_order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=new_order_body)


# Получение информации по новому заказу
def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, params={"t": track})
