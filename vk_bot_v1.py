import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def write_message(sender, message):
    authorize.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})


token = "efc42111e73ecc1d0a1f05e4d182628b74403b15b25eca2c48808b632b85f58dde9f7e4a081531a5dedda"
authorize = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(authorize, group_id=204249980)


# погода
# рифмы к имени

def say_hello():
    return f'Welcome! Ваш ID = {sender}'

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text') !="":
        reseived_message = event.message.get('text')
        sender = event.chat_id
        if reseived_message == "Привет":
            write_message(sender, say_hello())
        elif reseived_message == "Пока":
            write_message(sender, "До свидания!")
        else:
            continue
            # write_message(sender, "Я вас не понимаю...")
