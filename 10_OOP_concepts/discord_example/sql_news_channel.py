from channel import Channel


class SqlNewsChannel(Channel):
    name = 'SQL Channel 💾 -->'

    def send(self, msg):
        print(self.name, msg)
