import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from logpas import TOKEN
import random
import wikipedia


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195180475)
    wikipedia.set_lang('ru')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            id = event.obj.message['from_id']
            try:
                text = event.obj.message['text']
                print(text)
                message = (wikipedia.summary(text, sentences=2))
                print(message)
            except Exception:
                message = 'Не получилось найти ответ'
            vk.messages.send(user_id=id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
