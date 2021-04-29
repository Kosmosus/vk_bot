import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import datetime as dt


def write_message(sender, message):
    authorize.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})


token = "7f1964041bd040be8faf14cb84105d8e15fbd66fce3818dea0f9d3266df4b561abb9432810a44826d341f"
authorize = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(authorize, group_id=204293145)


def weather_time():
    moskow_time = dt.datetime.utcnow() + dt.timedelta(hours=3)
    weather_parameters = {
        '0': '',
        'T': '',
        'format': 2,
        'M': ''}

    request_headers = {'Accept-Language': 'ru'}
    response = requests.get('https://wttr.in/Novomoskovsk', params=weather_parameters, headers=request_headers)

    return 'Текущая дата: {0}\nТочное время: {1}\nПогода сейчас: {2}'\
        .format(moskow_time.strftime("%d.%m.%Y"), moskow_time.strftime("%H:%M:%S"), response.text)


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text') != "":
        reseived_message = event.message.get('text')
        sender = event.chat_id
        if reseived_message == "!погода":
            write_message(sender, weather_time())
        elif reseived_message == "Пока":
            write_message(sender, "До свидания!")
        else:
            continue
            # write_message(sender, "Я вас не понимаю...")
