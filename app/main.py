from __future__ import annotations
from typing import Union


class Distance:

    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __gt__(self, other: Union[int, float]) -> bool:
        return self.km > other

    def __lt__(self, other: Union[int, float]) -> bool:
        return self.km < other

    def __ge__(self, other: Union[int, float]) -> bool:
        return self.km >= other

    def __le__(self, other: Union[int, float]) -> bool:
        return self.km <= other

    def __eq__(self, other: Union[int, float]) -> bool:
        return self.km == other

    def __iadd__(self, other: Union[int, float, Distance]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> Distance:
        return Distance(round((self.km / other), 2))

    def __len__(self) -> int:
        return len(str(self.km))
