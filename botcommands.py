from info import *
import os


botid = 7004812988

def command(m): 
    if m.text == "/start":
        request(m)


def request(m):
    result = os.system('bash dump.sh')
    bot.reply_to(m, result)