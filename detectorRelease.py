import amino
import os

#
#CLIENT, LOGIN, SUBCLIENT
#
client = amino.Client()
client.login(email=os.getenv("email"), password=os.getenv("password"))
subclient = amino.SubClient(comId=os.getenv("comid"), profile=client.profile)
whitelist = []
with open('whitelist.txt', 'r') as file:
	for whitelistmember in file.readlines():
		whitelist.append(whitelistmember.strip())
print('Detector: ON')

def on_message(data):
#
#STRINGS
#
    chatid = data.message.chatId
    nickname = data.message.author.nickname
    content = str(data.message.content).split()
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
#
#Join
#
    if content[0][0] == '!':
        if content[0][1:].lower() == "join":
            if any(user in uid for user in whitelist):
                try:
                    print(content[-1])
                    id = client.get_from_code(content[-1]).objectId
                    subclient.join_chat(id)
                    subclient.send_message(chatId = chatid, message="Joined")
                except:
                    subclient.send_message(chatId = chatid, message="Error")
            else:
                subclient.send_message(chatId = chatid, message="You don't have permissions")
methods = []
for x in client.callbacks.chat_methods:
    methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))