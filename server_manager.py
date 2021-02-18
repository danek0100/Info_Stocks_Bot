# Импортируем созданный нами класс Server
from server import Server
# Получаем из config.py наш api-token
from config import vk_api_token



# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

# Data viz
import plotly.graph_objs as go

import time

from user import User
from user import ston

server = Server(vk_api_token, ..., "info_server")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера


USERS = []
user1 = User("Кирилл", id)
user2 = User("Матвей", id)

ston1 = ston("CSCO", 47, 10, 10)
ston2 = ston("F", 11.33, 10, 10)
ston3 = ston("AMD", 89.24, 10, 10)

ston4 = ston("F", 11, 2, 10)

user1.add_new_ston(ston1)
user1.add_new_ston(ston2)
user1.add_new_ston(ston3)

user2.add_new_ston(ston4)

USERS.append(user1)
USERS.append(user2)

for user in USERS:
    server.star_bot(user)
    server.your_active(user)

while 1:
    for user in USERS:
        for stonck in user.stons:
            data = yf.download(tickers=str(stonck.key), period="0")
            now = data['Close'][0]
            now = round(now, 4)
            print(now)

            if stonck.state == 0 and now > stonck.high_gr:
                server.time_to_sail(user, stonck.key, now)
                stonck.state = 1

            elif stonck.state == 1 and now < stonck.high_gr - 0.1 * stonck.high_gr:
                server.time_left(user, stonck.key, now)
                stonck.state = 0

            elif stonck.state == 0 and now < stonck.risk_gr:
                server.risk_high(user, stonck.key, now)
                stonck.state = 2

            elif stonck.state == 2 and now > now.risk_gr + 0.1 * stonck.risk_gr:
                server.have_chance(user, stonck.key, now)
                stonck.state = 0

            else:
                continue

    time.sleep(30)