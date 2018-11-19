import DiscordChat
import discord
import threading, time
import TwitchChat
from TwitchChat import TwitchChat
import irc.bot
from DiscordChat import DiscordChat
from datetime import datetime
import configparser
import os

class ChatRelay:
    def __init__(self):
        print("initializin ChatRelay program")
        self.configFile  = configparser .RawConfigParser() 
        dirname = os.path.dirname(__file__)
        configFilePath = os.path.join(dirname, 'Config.txt')
        self.configFile.read(configFilePath)

    def discordRelay(self, objDiscordChat,twitchMsgQueue):
        print("Initialize Discord Relay thread")
        while True:
            
            if twitchMsgQueue.qsize() > 0:
                print(twitchMsgQueue.qsize())
                message = twitchMsgQueue.get_nowait()
                print(message.username)
                objDiscordChat.send(message.message  , message.username)

    def TwitchRelay(self, objTwitchChat,discordMsgQueue):
        print("Initialize Twitch Relay thread")
        while True:
            time.sleep(19/30)
            if discordMsgQueue.qsize() > 0:        
                if objTwitchChat.messageCount < 20:
                    message = discordMsgQueue.get_nowait()
                    print("Message Count: {0}".format(objTwitchChat.messageCount))
                    if isinstance(message,discord.message.Message) :
                        objTwitchChat.send_MsgAsUserFromDiscord(message.content  ,message.author.name)
    def resetTimer(self,objTwitchChat,lastReset):
        while True:
            time.sleep(1)
            now = datetime.now()
            #print("Seconds: {0}".format((now - lastReset).seconds))
            if (now - lastReset).seconds >=30:
                print("Reset the timer and reset the counter")
                objTwitchChat.messagecount = 0
                lastReset = datetime.now()
                
    def run(self):
         
        print("hello ChatRelay program!")
        objDiscordChat = DiscordChat(int(self.configFile.get("Discord","WebHook_Id")),self.configFile.get("Discord","WebHook_Token"),self.configFile.get("Discord","DISCORD_BOT_TOKEN"),self.configFile.get("Discord","DISCORD_CHANNEL_NAME"))
        objTwitchChat = TwitchChat(self.configFile.get("Twitch","BotUserName"),self.configFile.get("Twitch","Client_id"),self.configFile.get("Twitch","Token"),self.configFile.get("Twitch","Channel"))
        
        taskDiscord = threading.Thread(target = objDiscordChat.run , name= "DiscordRecieveThread")
        taskDiscord.start()
        taskTwitch = threading.Thread(target = objTwitchChat.start , name= "TwitchRecieveThread")
        taskTwitch.start()
        lastReset = datetime.now()
        taskTwitchResetTimer = threading.Thread(target = self.resetTimer , name= "TwitchResetTimerThread", args=(objTwitchChat,lastReset))
        taskTwitchResetTimer.start()

        taskDiscord1 = threading.Thread(target = self.discordRelay , name= "DiscordSendThread", args= (objDiscordChat,objTwitchChat.messageQueue))
        taskDiscord1.start()
        taskTwitch1 = threading.Thread(target = self.TwitchRelay , name= "TwitchSendThread", args= (objTwitchChat,objDiscordChat.messageQueue))
        taskTwitch1.start()
        
        
     
        
