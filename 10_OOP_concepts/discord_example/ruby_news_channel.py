from channel import Channel

class RubyNewsChannel(Channel):
    name = '💎 Ruby Daily 💎'

    def send(self, msg):
        print(self.name, msg)
