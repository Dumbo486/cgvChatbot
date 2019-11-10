import telegram

bot = telegram.Bot(token = '816580560:AAENpbomNq7kMD-XZ7ujC1z-Oid9AW2Qjog')
# for i in bot.get_updates():
#     print(i.message)

bot.send_message(chat_id = 568425088, text="덤보테스트")