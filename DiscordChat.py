import requests
import discord
import emoji
from discord import Webhook, RequestsWebhookAdapter
import asyncio 
from asyncio import Queue
import SmilieMap
from SmilieMap import SmilieTranslation

class DiscordChat:
    def __init__(self,webHookId,WebHookToken,DiscordBotToken,ChannelName):
        self.messageQueue = Queue()
        self.client = discord.Client()
        self.on_ready = self.client.event(self.on_ready)
        self.on_message  = self.client.event(self.on_message)
        self.channelName = ChannelName
        self.WEBHOOK_ID = webHookId  
        self.WEBHOOK_TOKEN = WebHookToken  
        self.DISCORD_BOT_TOKEN = DiscordBotToken 
        self.__webhook = Webhook.partial(self.WEBHOOK_ID, self.WEBHOOK_TOKEN,adapter=RequestsWebhookAdapter())
        self.emojiTranslator = SmilieTranslation()

    def send(self, message,username):
        self.__webhook.send(message, username=username)
  
    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('------')
        
    async def on_message(self,message):
        if message.channel.name == self.channelName:
            if message.author == self.client.user:
                return
            if message.author.bot:
                return
            message.content = self.translateEmoji(message.content)
            self.messageQueue.put_nowait(message)

    def run(self):
        self.client.run(self.DISCORD_BOT_TOKEN)

       
    def translateEmoji(self,discordTextWithEmoji):
        returnval = self.emojiTranslator.translateDiscordSmilie(discordTextWithEmoji)
        return returnval
        
