import amino
import os

client = amino.Client()
client.login(email=os.getenv("email"), password=os.getenv("password"))
subclient = amino.SubClient(comId=os.getenv("comid"), profile=client.profile)
print('Detector: ON')

def on_message(data):
    chatid = data.message.chatId
    nickname = data.message.author.nickname
    content = data.message.content
    mtype = data.message.type
    mid = data.message.messageId
    uid = data.message.author.userId
#
#ANTIRAID
#
    if (mtype == 100) | (mtype == 109) | (mtype == 107)  | (mtype == 110) | (mtype == 108)  | (mtype == 111) | (mtype == 111):
        if mtype == 100 and content == None:
                  pass
        else:
            subclient.kick(chatId=chatid, userId = uid, allowRejoin=False)
            subclient.send_message(chatId = chatid, message = f'MessageType {mtype} detected! Nickname: {nickname} | userId: {uid} | messageId: {mid}.')
#
#HEY
#
    if content == "?hey":
        subclient.send_message(chatId=chatid, message="work status: True")
methods = []
for x in client.callbacks.chat_methods:
    methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))