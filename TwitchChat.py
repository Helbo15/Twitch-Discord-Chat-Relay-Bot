import asyncio 
from asyncio import Queue
import irc.bot
import SmilieMap
from SmilieMap import SmilieTranslation

class TwitchChat(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.messageQueue = Queue()
        self.emojiTranslator = SmilieTranslation()
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.messageCount =0
        server = 'irc.chat.twitch.tv'
        port = 6667
        print("Attempting to connect to {0} on port {1} ...".format(server,port))
        oauthToken = 'oauth:{0}'.format(token)
        print(oauthToken)
        print(username)
        irc.bot.SingleServerIRCBot.__init__(self,[(server,port,oauthToken)],username,username)

    def on_welcome(self,conn,event):
        print("Joining {0}".format(self.channel))

        conn.cap('REQ', ':twitch.tv/membership')
        conn.cap('REQ', ':twitch.tv/tags')
        conn.cap('REQ', ':twitch.tv/commands')
        conn.join(self.channel)
        self.conn= conn

    def on_pubmsg(self, conn, event):
        print("text Recived: {0} from channel: {1}".format(event.arguments[0],self.channel))
        print("text Recived: {0} from channel: {1}".format(event.tags[2].get('value'),self.channel))
        self.messageQueue.put_nowait(message('[' + event.tags[2].get('value')+'] ',self.emojiTranslator.translateTwitchSmilie(event.arguments[0])) )
        
    def send_MsgAsUserFromDiscord(self, message, username):
        self.messageCount +=1 
        self.conn.privmsg(self.channel, '[DC-' + username + ']: ' + message)
        

class message:
    def __init__(self,username,message):
        self.username = username
        self.message = message
