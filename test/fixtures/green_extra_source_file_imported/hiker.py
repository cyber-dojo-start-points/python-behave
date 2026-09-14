from checksum import checksum


class Hiker:

    def answer(self: Hiker, first: int, second: int) -> int:
        return first * checksum()
