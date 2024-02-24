from info import *
import random
import os

dump_methods = ["dump_crave.sh", "dump_gh_actions.sh"]
botid = 7004812988
request_id = -1001263694109

def command(m): 
    if m.text == "/start":
        bot.reply_to(m, "Hi, if you want to use me please join here: https://t.me/+_uajqfCeH6Y4ZWJl")
    if m.text.split()[0] =="/request":
        if m.chat.id == request_id:
            request(m)
        else:
            bot.reply_to(m, "Please join this group and use me there: https://t.me/+_uajqfCeH6Y4ZWJl")

def request(m):
    try:
        URL = m.text.split()[1]
        dump_method = random.choice(dump_methods)
        result = os.system(f'bash {dump_method} {URL}')
        if result == 0:
            bot.reply_to(m, "Succesfully requested the dump!")
        else:
            bot.reply_to(m, "Something went wrong")
    except:
        bot.send_message(m.chat.id, "I need a url to work")