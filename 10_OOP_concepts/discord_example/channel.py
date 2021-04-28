from abc import ABC, abstractmethod


class Channel(ABC):
    @abstractmethod
    def send(self, msg: str):
        print('Bot 🤖 :', msg)