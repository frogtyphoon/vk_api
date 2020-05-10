import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from logpas import TOKEN, LOGIN, PASSWORD
import random


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
    pics = []
    if response['items']:
        for pic in response['items']:
            pics.append(f'photo{pic["owner_id"]}_{pic["id"]}')

    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195180475)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            id = event.obj.message['from_id']
            vk = vk_session.get_api()
            user = vk.users.get(user_ids=id, fields='city')
            message = "Привет, {}".format(user[0]["first_name"])
            vk.messages.send(user_id=id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64),
                             attachment=[random.choice(pics)])


if __name__ == '__main__':
    main()
