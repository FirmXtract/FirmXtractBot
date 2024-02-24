from info import *
import os


botid = 7004812988

def command(m): 
    if m.text == "/start":
        request(m)


def request(m):
    result = os.system('bash dump.sh')
    if result == 0:
        bot.reply_to(m, "Succesfully requested the dump!")
    else:
        bot.reply_to(m, "Something went wrong")