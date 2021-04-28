from discord_connector import DiscordConnector
from python_news_channel import PythonNewsChannel
from ruby_news_channel import RubyNewsChannel
from sql_news_channel import SqlNewsChannel

if __name__ == '__main__':
    py_news_channel = PythonNewsChannel()

    d = DiscordConnector()
    d.post_news(py_news_channel, 'Now you can use emoji in Python! WOW')

    print('------------')

    rb_news_channel = RubyNewsChannel()
    d.post_news(rb_news_channel, 'Ruby 3.0 is live!')

    print('------------')

    sql_news_channel = SqlNewsChannel()
    d.post_news(sql_news_channel, 'My favorite SQL DB is psql :)')
