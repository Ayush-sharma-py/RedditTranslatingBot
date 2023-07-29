import praw
from googletrans import *

with open("TranslateCredential.txt","r") as f:
    credentials = f.read().split(";")

reddit = praw.Reddit(client_id=credential[0],
                     client_secret=credential[1],
                     password=credential[2],
                     user_agent=credential[3],
                     username=credential[4]
                    )

translator = Translator() 

if reddit.user.me() == #username:
    print("Authentication Sucessfull") 


ban_list = []
with open("translate_bot.txt","r") as f:
    data = f.read()
    f.close()

data = data.split(",")
for i in data:
    ban_list.append(i)


while True:
    for mention in reddit.inbox.mentions():
        try:
            if mention not in  ban_list:
                parent = mention.parent_id
                parent = parent.split("_")[1]
                comment = reddit.comment(parent)
                comment_text = comment.body
                comment_text = translator.translate(comment_text)
                mention.reply(comment_text.text)
                print("one")
                ban_list.append(mention)
                with open("translate_bot.txt","a") as f:
                    f.write("," + str(mention))
                    f.close()
                break
            else:
                print("No New")
        except:
            print("Waiting")
            break


