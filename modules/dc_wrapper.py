import discord
import dc_actions
from typing import Tuple
from logging import getLogger, DEBUG, StreamHandler
from dataclasses import dataclass

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.addHandler(handler)


class MsgLogger:
    """メッセージを取得するロガークラス

    Note: TODO 現状不要メッセージのロガーだが色々機能積みたい
    """

    def execute(msg):
        logger.info(msg)


@dataclass
class DiscordWrapper:
    """Discord.pyのラッパークラス"""

    client = discord.Client()

    @client.event
    async def on_ready(self):
        logger.info("Ready to Discord Py Bot")

    @client.event
    async def on_message(self, message):
        msg_action = self.parse_message(message)
        if msg_action[0]:
            msg = msg_action[1].execute(msg_action[2])
            logger.info(f"Send to {msg}")
            await message.channel.send(msg)
        logger.info(f"Get log message: {message}")
        await msg_action[1].execute(msg_action[2])

    def parse_message(message: str) -> Tuple[int, str, str]:
        """受信メッセージの接頭語をもとに解析する

        Args:
            message (str): 受信メッセージ

        Returns:
            Tuple[int, str, str]: フラグとアクションと受信メッセージ
        """
        for action in dc_actions.Actions:
            msg = message.content.split("/")
            if msg[0] == action.name:
                return 1, action.value, msg[1]
        # 関係のない文章をログとして取れるようにしたいため
        return 0, MsgLogger(), message
