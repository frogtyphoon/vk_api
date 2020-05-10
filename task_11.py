import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from logpas import TOKEN
import random
import requests
import sys
from datetime import datetime


def get_object_size(geo_object):
    lower_corner = list(map(float, geo_object['boundedBy']['Envelope']['lowerCorner'].split()))
    upper_corner = list(map(float, geo_object['boundedBy']['Envelope']['upperCorner'].split()))
    return (str(abs(lower_corner[0] - upper_corner[0]) / 2),
            str(abs(lower_corner[1] - upper_corner[1]) / 2))


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 195180475)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            id = event.obj.message['from_id']
            vk = vk_session.get_api()
            toponym_to_find = event.obj.message['text']
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": toponym_to_find,
                "format": "json"}

            response = requests.get(geocoder_api_server, params=geocoder_params)

            if not response:
                print("Ошибка выполнения запроса:")
                print(geocoder_api_server)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            map_file = "static/img/map.png"
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

            delta = get_object_size(toponym)

            # Собираем параметры для запроса к StaticMapsAPI:
            map_params = {
                'll': ','.join([toponym_longitude, toponym_lattitude]),
                'spn': ",".join([delta[0], delta[1]]),
                'l': 'map',
                'pt': ','.join([toponym_longitude, toponym_lattitude, 'flag'])
            }

            map_api_server = "http://static-maps.yandex.ru/1.x/"
            static_response = requests.get(map_api_server, params=map_params)

            with open(map_file, "wb") as file:
                file.write(static_response.content)

            vk.messages.send(user_id=id,
                             message=f' Это {toponym_to_find}. Что вы еще хотите увидеть?',
                             random_id=random.randint(0, 2 ** 64),
                             keyboard=open("keyboard/ans_keyboard.json", "r", encoding="UTF-8").read(),
                             attachements=['static/img/map.png'])


if __name__ == '__main__':
    main()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы
