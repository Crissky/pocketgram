from typing import List, Union

from pocketgram.status.status import MajorStatus, MinorStatus


class Conditions:
    def __init__(
        self,
        major_status: Union[MajorStatus, str] = None,
        minor_status: Union[MinorStatus, str, List[MinorStatus, str]] = None,
    ):
        if isinstance(major_status, str):
            major_status = MajorStatus[major_status]
        if not isinstance(major_status, MajorStatus):
            raise TypeError(
                f'"major_status" não é um MajorStatus válido. '
                f"Tipo: {type(major_status)}"
            )

        if isinstance(minor_status, MinorStatus):
            minor_status = [minor_status]
        elif isinstance(minor_status, str):
            minor_status = [MinorStatus[minor_status]]
        if isinstance(minor_status, list):
            for index in range(len(minor_status)):
                ms = minor_status[index]
                if isinstance(ms, str):
                    minor_status[index] = MinorStatus[ms]
                if not isinstance(ms, MinorStatus):
                    raise TypeError(
                        f'Elemento da lista "minor_status" ({index}) não é um '
                        f"MinorStatus válido. Tipo: {type(ms)}"
                    )

        self.major_status = major_status
        self.minor_status_list = minor_status or []
