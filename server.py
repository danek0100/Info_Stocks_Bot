# For bot
import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

import vk
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

from config import vk_api_token

vk_session = vk_api.VkApi(token=vk_api_token)
Lslongpoll = VkBotLongPoll(vk_session, group_id=)



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

    def star_bot(self, user):
        rand = get_random_id()
        self.send_msg(user.id, str(user.name) + ", бот запущен!", rand)

    def risk_high(self, user, stonck, price_now):
        rand = get_random_id()
        self.send_msg(user.id, str(user.name) + ", пробит нижний порог, пора продавать!\n"
                                                "Акция " + str(stonck) + " - " + str(price_now) + '$', rand)

    def time_to_sail(self, user, stonck, price_now):
        rand = get_random_id()
        self.send_msg(user.id, str(user.name) + ", достигнут верхний порог прибыли, пора забирать деньги!\n"
                                                "Акция " + str(stonck) + " - " + str(price_now) + '$', rand)

    def time_left(self, user, stonck, price_now):
        rand = get_random_id()
        self.send_msg(user.id, str(user.name) + ", время упущенно, денги ушли!\n"
                                                "Акция " + str(stonck) + " - " + str(price_now) + '$', rand)

    def have_chance(self, user, stonck, price_now):
        rand = get_random_id()
        self.send_msg(user.id, str(user.name) + ", цена стабилизировалсь, у вас есть шансы!\n"
                                                "Акция " + str(stonck) + " - " + str(price_now) + '$', rand)

    def your_active(self, user):
        for stonck in user.stons:
            rand = get_random_id()
            self.send_msg(user.id, "Вы купили " + str(stonck.key) + " за " + str(stonck.start_price) + " $", rand)


