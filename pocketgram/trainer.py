from pocketgram.enums.badge import BadgeEnum


class Trainer:

    def __init__(
        self,
        _id: str,
        user_id: str,
        user_name: str,
        badge_list: list[BadgeEnum] = None,
    ):
        if badge_list is None:
            badge_list = []

        self._id = _id
        self.user_id = user_id
        self.user_name = user_name
        self.badge_list = badge_list
