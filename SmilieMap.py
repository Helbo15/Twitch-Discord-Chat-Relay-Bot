import discord 
class SmilieTranslation:

    def __init__(self):
        self.TwitchDiscordSmilies ={':)':":smiley:",':(':':frowning:',':o':':open_mouth:',':O':':open_mouth:',':Z':':unamused:',':z':':unamused:','B)':':sunglasses:',':/':':confused:',';)':':wink:',';P':':stuck_out_tongue_winking_eye:',';p':':stuck_out_tongue_winking_eye:',':P':':stuck_out_tongue:',':p':':stuck_out_tongue:','R)':':construction_worker:','o_O':':astonished:',':D':':smile:','>(':':rage:','<3':':heart:'}
        self.DiscordTwitchSmilies ={"😃":':)','😦':':(','😮':':O','😒':':z','😎':'B)','😕':':/','😉':';)','😜':';p','😛':':p','👷':'R)','😲':'o_O','😄':':D','😡':'>(','❤':'<3'}
        
    def translateTwitchSmilie(self,sentence):
        for key in self.TwitchDiscordSmilies:
           sentence = sentence.replace(key,self.TwitchDiscordSmilies[key])
        return sentence

    def translateDiscordSmilie(self,sentence):
        for key in self.DiscordTwitchSmilies:
           sentence = sentence.replace(key,self.DiscordTwitchSmilies[key])
        return sentence
