from dataclasses import dataclass
from typing import List
import random
import csv


@dataclass
class GachaDataManager:
    """ガチャのデータを管理するクラス"""

    name: str
    appearance: int
    appearance_ten: int
    star: int


class ContentsDownloader:
    """ガチャ提供内容のダウンローダー"""

    @classmethod
    def download(cls, csv_name: str):
        with open(csv_name) as f:
            return Formatter.format_gacha_data(f)


class Formatter:
    """各種フォーマットの変換を行うクラス"""

    @classmethod
    def format_gacha_data(cls, f):
        gacha_contents: List[GachaDataManager()] = []
        next(csv.reader(f))
        for row in csv.reader(f):
            gacha_data = GachaDataManager(
                row[0], float(row[1]), float(row[2]), int(row[3])
            )
            gacha_contents.append(gacha_data)
        return gacha_contents

    @classmethod
    def format_name_list(cls, contents) -> List[str]:
        name_list = []
        for data in contents:
            name_list.append(data.name)
        return name_list

    @classmethod
    def format_name_list_excpet_star(cls, contents) -> List[str]:
        name_list = []
        for data in contents:
            if data.star != 1:
                name_list.append(data.name)
        return name_list

    @classmethod
    def format_appearance_list(cls, contents) -> List[float]:
        appearance_list = []
        for data in contents:
            appearance_list.append(data.appearance)
        return appearance_list

    @classmethod
    def format_appearance_list_except_star(cls, contents) -> List[float]:
        appearance_list = []
        for data in contents:
            if data.star != 1:
                appearance_list.append(data.appearance_ten)
        return appearance_list


class GachaSimulator:
    """ガチャのシミュレーションを行うクラス"""

    @classmethod
    def simulate(cls, times: int, contents) -> List[str]:
        result: List[str]
        names = Formatter.format_name_list(contents)
        names_ten = Formatter.format_name_list_excpet_star(contents)
        appearance = Formatter.format_appearance_list(contents)
        appearance_ten = Formatter.format_appearance_list_except_star(contents)
        if times == 10:
            result = random.choices(names, k=9, weights=appearance)
            result_ten = random.choices(names_ten, k=1, weights=appearance_ten)
            result.extend(result_ten)
        elif times >= 1 and times <= 9:
            result = random.choices(names, k=times, weights=appearance)
        else:
            pass
        return result


def play_purikone_gacha(times: int):
    purikone_contents = ContentsDownloader.download(
        "/home/kissy24/workspace/gacha/purikone_gacha.csv"
    )
    gacha_result: List[str] = GachaSimulator.simulate(times, purikone_contents)
    return gacha_result


def main():
    times: int = int(input())
    gacha_result = play_purikone_gacha(times)
    for name in gacha_result:
        print(name)


if __name__ == "__main__":
    main()