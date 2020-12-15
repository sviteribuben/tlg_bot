# pip install aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# get token in BotFather
bot = Bot(token='977459387:AAFN1xXIN7Lb6rV2uyJWeHmXU6GZhWfIZeU')

# в боте создался поток в котором будет работать диспатчер
# диспатчер принимает поток бота и забирает из него loop
# чтобы передавать все апдейты пишем хендлеры для того чтобы их ловить
# создаем объект диспатчера
dp = Dispatcher(bot)
# декоратор для текстовых соообщений
# этот хэндлер будет принимать ВСЕ сообщения
@dp.message_handler()

async def get_message(message: types.Message):
    # chat_id = message.chat.id
    # text = 'Хуй саси'
    # # сохраняем результат отправки сообщеня в переменную
    # send_message = await bot.send_message(chat_id=chat_id, text=text)
    # # chat_id достаем из message
    # # распечатаем как словарь
    # print(send_message.to_python())

    # отправка фото в чат

    # chat_id = -1001157752263
    # sent_message = await bot.send_photo(chat_id=chat_id, photo='https://cs12.pikabu.ru/post_img/2020/12/15/6/1608025748177290148.png')
    # print(sent_message.photo[-1].file_unique_id)

    # новое название для чата
    # title = 'DIY_CHE'
    # result = await bot.set_chat_title(chat_id=-1001157752263, title=title)
    # print(result)

    # достать инвайт линк для чата
    # invite_link = await bot.export_chat_invite_link(chat_id=-1001157752263)
    # print(invite_link)

    # получить юзернейм бота
    bot_user = await bot.get_me()
    print(bot_user.username)

# import executor to get all updates
# передаем диспатчер в executor
# в executor сбор апдейтов и их проработка до попадания в хэндлер
executor.start_polling(dp)




