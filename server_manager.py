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


server1 = Server(vk_api_token, 202539555, "info_server")
# vk_api_token - API токен, который мы ранее создали
# 172998024 - id сообщества-бота
# "server1" - имя сервера


# написать бота, который будет писать сообщения, когда прибыль привысит 3%
open = 47.1316

server1.star_bot()
server1.your_price(open)

while 1:
    # Купили за 1685,6
    data = yf.download(tickers='CSCO', period="0")
    now = data['Close'][0]
    # print(data)
    print(now)

    if now > open + open * 0.001:
        server1.time_to_sale()
        while now > open + open * 0.0005:

            data = yf.download(tickers='CSCO', period="0")
            now = data['Close'][0]
            if now < open + open * 0.005:
                server1.time_left()
                break
            time.sleep(30)

    elif now < open - open * 0.001:
        server1.risk_high()
        while now < open - open * 0.0005:

            data = yf.download(tickers='CSCO', period="0")
            now = data['Close'][0]
            if now > open - open * 0.0005:
                server1.have_chance()
                break
            time.sleep(30)

    time.sleep(30)
