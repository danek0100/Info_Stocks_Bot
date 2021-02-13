# For bot
import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

import random


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

    def star_bot(self):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Бот запущен!", rand)

    def risk_high(self):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Пробит нижний порог, пора продавать!", rand)

    def time_to_sail(self):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Достигнут верхний порог прибыли, пора забирать деньги!", rand)

    def time_left(self):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Время упущено, деньги ушли!", rand)

    def have_chance(self):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Цена стабилизировалось, вы имеете шансы!", rand)

    def your_price(self, price):
        rand = random.randint(0, 2147483646)
        self.send_msg(151726618, "Вы купили за " + str(price) + " $", rand)