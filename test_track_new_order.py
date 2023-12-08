# Елизавета Кожарская, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Сохранение номера трека заказа
def get_track_new_order():
    track = sender_stand_request.post_new_order(data.new_order_body)
    return track.json()["track"]


# Тест на получение заказа по треку заказа
def test_get_new_order_by_track():
    track = get_track_new_order()
    response = sender_stand_request.get_new_order(track)
    #  Проверяем, что код ответа равен 200
    assert response.status_code == 200
