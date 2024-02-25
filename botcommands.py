from info import *
import random
import os

dump_methods = ["dump_crave.sh", "dump_gh_actions.sh"]
botid = 7004812988
request_id = -1001263694109

def command(m): 
    if m.text == "/start":
        bot.reply_to(m, "Hi, if you want to use me please join here: https://t.me/+_uajqfCeH6Y4ZWJl")
        bot.send_message(m.chat.id, f"This bot is made by {bot_creator}")
    if m.text.split()[0] =="/request":
        if m.chat.id == request_id:
            request(m)
        else:
            bot.reply_to(m, "Please join this group and use me there: https://t.me/+_uajqfCeH6Y4ZWJl")

def request(m):
    try:
        URL = m.text.split()[1]
        with open("requested_URLs.txt","r",encoding="utf-8") as tx:
            for i in tx.readlines():
                print(i)
                if i == URL:
                    bot.reply_to(m, "This FW has been requested before, make sure that what you're requesting a FW that isn't actually dumped")
                else:
                    f_replytxt=open("requested_URLs.txt","a",encoding="utf-8")
                    f_replytxt.write("\n")
                    f_replytxt.write(URL)
                    f_replytxt.close()
                    dump_method = random.choice(dump_methods)
                    result = os.system(f'bash {dump_method} {URL}')
                    if result == 0:
                        bot.reply_to(m, "Succesfully requested the dump!")
                    else:
                        bot.reply_to(m, "Something went wrong")
    except FileNotFoundError:
        bot.reply_to(m, "Fatal error, contact admins!!!")
    except IndexError:
        bot.reply_to(m, "I need a url to work")