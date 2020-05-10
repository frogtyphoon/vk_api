import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from logpas import TOKEN
import random
from datetime import datetime


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195180475)
    weekdays = ["понедельник", "вторник", "стреда", "четверг", "пятница", "суббота", "воскресенье"]
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            id = event.obj.message['from_id']
            vk = vk_session.get_api()
            try:
                dt = datetime.strptime(event.obj.message['text'], "%Y-%m-%d")
                message = '{}'.format(weekdays[dt.weekday()])
            except Exception:
                message = 'Могу отправить какой день недели по дате в формате YYYY-MM-DD'
            vk.messages.send(user_id=id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
