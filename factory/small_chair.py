# pylint: disable=too-few-public-methods
"A Class of Chair"
from interface_chair import IChair


class SmallChair(IChair):
    "The Small Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self._height = 30
        self._width = 30
        self._depth = 30

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }
