class DiscordConnector:
    def __init__(self):
        print('Loguję się do Discorda')

    def post_news(self, channel, msg):
        channel.send(msg)

