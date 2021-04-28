from channel import Channel


class PythonNewsChannel(Channel):
    def send(self, msg):
        print("🐍", msg)


