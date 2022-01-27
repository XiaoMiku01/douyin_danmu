import time

from . import message_pb2
from . import base


class MemberMessage(base.Base):
    def __init__(self):
        self.instance = message_pb2.MemberMessage()

    def format_content(self):
        template = self.instance.common.displayText.defaultPattern
        nickname = self.user().nickname

        return template.replace('{0:user}', nickname).replace('{1:string}', '')

    def __str__(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '【进入直播间】' + self.format_content()
