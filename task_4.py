import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from logpas import TOKEN
import random


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195180475)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            id = event.obj.message['from_id']
            vk = vk_session.get_api()
            user = vk.users.get(user_ids=id, fields='city')
            message = "Привет, {}\n" \
                      "Как поживает {}?".format(user[0]["first_name"],
                                                (user[0]["city"]["title"] if "city" in user[0] else ''))
            vk.messages.send(user_id=id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
