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
    # Используем метод wall.get
    response = vk.wall.get(count=5)
    if response['items']:
        for post in response['items']:
            print('{};\n'
                  'date: {}, time: {}'.format(post["text"],
                                              datetime.utcfromtimestamp(post["date"]).strftime('%Y-%m-%d'),
                                              datetime.utcfromtimestamp(post["date"]).strftime('%H:%M:%S')))


if __name__ == '__main__':
    main()
