from info import *
import os


botid = 7004812988

def command(m): 
    if m.text == "/start":
        bot.reply_to(m, "Hi, if you want to use me please join here: https://t.me/+_uajqfCeH6Y4ZWJl")
    if m.text =="/request":
        request(m)


def request(m):
    try:
        URL = m.text.split()[1]
        result = os.system(f'bash dump.sh {URL}')
        if result == 0:
            bot.reply_to(m, "Succesfully requested the dump!")
        else:
            bot.reply_to(m, "Something went wrong")
    except:
        bot.reply_to(m, "I need a url to work")