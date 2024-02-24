from info import *
import os


botid = 7004812988
request_id = -1001263694109

def command(m): 
    if m.text == "/start":
        bot.reply_to(m, "Hi, if you want to use me please join here: https://t.me/+_uajqfCeH6Y4ZWJl")
    if m.text =="/request":
        if m.chat.id == request_id:
            request(m)
        else:
            bot.reply_to(m, "Please join this group and use me there: https://t.me/+_uajqfCeH6Y4ZWJl")

def request(m):
    # try:
    #     URL = m.text.split()[1]
    os.system('bash dump.sh')
    #     if result == 0:
    #         bot.reply_to(m, "Succesfully requested the dump!")
    #     else:
    #         bot.reply_to(m, "Something went wrong")
    # except:
    #     bot.send_message(m.chat.id, "I need a url to work")