# For bot
import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

import vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

from config import vk_api_token

vk_session = vk_api.VkApi(token=vk_api_token)
Lslongpoll = VkBotLongPoll(vk_session, group_id=202539555)



def create_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard(one_time=False)
    # False Если клавиатура должна оставаться откртой после нажатия на кнопку
    # True если она должна закрваться

    keyboard.add_button("Закрыть", color=vk_api.keyboard.VkKeyboardColor.DEFAULT)
    keyboard.add_button("Кнопка", color=vk_api.keyboard.VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Обозначает добавление новой строки
    keyboard.add_button("Кнопка", color=vk_api.keyboard.VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button("Кнопка", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)
    keyboard.add_button("Кнопка", color=vk_api.keyboard.VkKeyboardColor.PRIMARY)

    return keyboard.get_keyboard()
    # Возвращает клавиатуру


# Эта функция используется для закрытия клавиатуры
def create_empty_keyboard():
    keyboard = vk_api.keyboard.VkKeyboard.get_empty_keyboard()
    return keyboard

def send_messages(user_id, msg, attachments):
    vk_session.method('messages.send', {'user_id': user_id,
                                        'random_id': get_random_id(),
                                        'message': msg,
                                        'attachment': attachments,
                                        'keyboard': None})
class Server:

    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        # Даем серверу имя
        self.server_name = server_name

        # Для Long Poll
        self.vk = vk_api.VkApi(token=api_token)

        # Для использования Long Poll API
        self.long_poll = VkBotLongPoll(self.vk, group_id)

        # Для вызова методов vk_api
        self.vk_api = self.vk.get_api()

    def send_msg(self, send_id, message, rand):
        self.vk_api.messages.send(user_id=send_id,
                                  random_id=rand,
                                  message=message)

    #def StartKeyBoard(self):
     #   for event in Lslongpoll.listen():
       #     if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
         #       try:
           #         print(event.obj.from_id)
            #        print("Текст Сообщения: " + str(event.obj.text or event.message.text))
             #       print('*' * 30)
              #      response = event.obj.text.casefold() or event.message.text.casefold()
               #     keyboard = create_keyboard()
                #    empty_keyboard = create_empty_keyboard()
               # finally:
                #    empty_keyboard = create_empty_keyboard()

    def star_bot(self):
        rand = get_random_id()
        self.send_msg(151726618, "Бот запущен!", rand)

    def risk_high(self):
        rand = get_random_id()
        self.send_msg(151726618, "Пробит нижний порог, пора продавать!", rand)

    def time_to_sail(self):
        rand = get_random_id()
        self.send_msg(151726618, "Достигнут верхний порог прибыли, пора забирать деньги!", rand)

    def time_left(self):
        rand = get_random_id()
        self.send_msg(151726618, "Время упущено, деньги ушли!", rand)

    def have_chance(self):
        rand = get_random_id()
        self.send_msg(151726618, "Цена стабилизировалось, вы имеете шансы!", rand)

    def your_price(self, price):
        rand = get_random_id()
        self.send_msg(151726618, "Вы купили за " + str(price) + " $", rand)


