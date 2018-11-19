import ChatRelay
from ChatRelay import ChatRelay


class TDCRBot:
    def __init__(self):
        print("initializin main program")
        
    def run(self):
        print("Running program!")
        self.main()
        
    def main(self):
        print("hello from Main program!")  

        objDChatRelay = ChatRelay()
        objDChatRelay.run()
        

if __name__ == "__main__":
    app = TDCRBot()
    app.run()
