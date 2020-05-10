import vk_api
from logpas import LOGIN, PASSWORD
import os
from datetime import datetime


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    # Используем метод
    vk = vk_session.get_api()
    response = vk.photos.get(album_id=272100032, group_id=195180475)
    if response['items']:
        for pic in response['items']:
            print(pic["sizes"][0]["url"], 'width:', pic["sizes"][0]["width"], 'height:', pic["sizes"][0]["height"])


if __name__ == '__main__':
    main()
