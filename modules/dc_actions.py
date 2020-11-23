from enum import Enum
from typing import List
from modules.actions.gacha import ContentsDownloader, GachaSimulator


class GachaExecuter:
    """ガチャモジュールの呼び出しクラス

    Note:
        - excute()の
            - 引数は1つでstr型
            - 返り値はstr型
    """

    def execute(times: str) -> str:
        # TODO 絶対パスベタ打ちそのうち直す
        purikone_contents = ContentsDownloader.download(
            "/home/kissy24/workspace/discord-pybot/modules/files/purikone_gacha.csv"
        )
        if not times.isdecimal():
            return "メッセージが不正です"
        gacha_result: List[str] = GachaSimulator.simulate(int(times), purikone_contents)
        return " ".join(gacha_result)


class Actions(Enum):
    """Discordの接頭語に対応するActionの列挙体

    Note:
        - 左辺: メッセージの接頭語(ex. bhoge)
            - メッセージ例: bhoge/hogehoge
        - 右辺: 起動したいクラス(ex. HogeExecuter)
            - ダックタイピング採用のためexecute()必須
    """

    bgacha = GachaExecuter
