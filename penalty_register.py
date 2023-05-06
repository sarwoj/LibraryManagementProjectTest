from typing import Dict, List
from penalty import Penalty
from reader import Reader


class PenaltyRegister:
    _penalities: Dict[int, List[Penalty]]

    def __init__(self) -> None:
        self._penalities = {}

    def add_penalty(self, reader: "Reader", penalty: "Penalty"):
        if not self._penalities.get(reader.number):
            self._penalities[reader.number] = []
        self._penalities[reader.number].append(penalty)

    def check_for_penalty(self, reader):
        if not self._penalities.get(reader.number):
            return False
        return True
