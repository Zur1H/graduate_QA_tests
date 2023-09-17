# Шумилин Никита, 8-я когорта, Дипломный проект. Инженер по тестированию плюс
import order_by_track


def test_get_order():
    response = order_by_track.post_new_order()
    track = response.json()["track"]

    response = order_by_track.get_order(track)
    assert response.status_code == 200
    