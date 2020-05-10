import vk_api
from logpas import LOGIN, PASSWORD
from datetime import datetime


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод friends.get
    response = vk.friends.get(fields="bdate")
    friends = []
    if response['items']:
        for friend in response['items']:
            friends.append(friend)
    friends.sort(key=lambda x: x["last_name"])
    for friend in friends:
        print(friend["last_name"], friend["first_name"], friend["bdate"] if "bdate" in friend else 'Не указано')


if __name__ == '__main__':
    main()
