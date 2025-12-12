from pocketgram.enums.status import StatusEnum


class Status:
    def __init__(self, status: StatusEnum):
        self.status = status


class MajorStatus(Status):
    ...


class MinorStatus(Status):
    ...
