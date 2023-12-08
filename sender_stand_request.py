import configuration
import requests
import data


# Создание нового заказа
def post_new_order(new_order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=new_order_body)
response = post_new_order(data.new_order_body)
print(response.status_code)
print(response.json())


# Получение информации по новому заказу
def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, params={"t": track})
response = get_new_order(data.new_order_body)
print(response.status_code)
print(response.json())
