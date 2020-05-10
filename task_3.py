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
    upload = vk_api.VkUpload(vk_session)
    for img in os.listdir('static/img/'):
        upload.photo(f'static/img/{img}', 804751951, 195180475)


if __name__ == '__main__':
    main()
