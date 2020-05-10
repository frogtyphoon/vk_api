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
    possible_answers = ['время', 'число', 'дата', 'день']
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            id = event.obj.message['from_id']
            vk = vk_session.get_api()
            if event.obj.message['text'].lower() in possible_answers:
                message = '{} {}'.format(datetime.now().strftime('%Y-%m-%d %{}:%M:%S'.format(datetime.now().hour - 4)),
                                         weekdays[datetime.now().weekday()])
            else:
                message = 'Могу отправить временные данные\nПросто отправь один из маркеров:время, число, дата, день'
            vk.messages.send(user_id=id,
                             message=message,
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
