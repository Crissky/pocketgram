
from pocketgram.enums.badge import BadgeEnum


class Trainer:

    def __init__(
        self,
        name: str,
        nickname: str,
        badge_list: list[BadgeEnum] = None,
    ):
        if badge_list is None:
            badge_list = []

        self.name = name
        self.nickname = nickname
        self.badge_list = badge_list
