import sys


class Hiker:

    def answer(self: Hiker, first: int, second: int) -> int:
        # The learner is watching the call happen and has not taken this out
        # yet. behave captures both streams for the duration of a step and
        # throws the capture away when the step passes, so a green run never
        # shows this line.
        print('answer was called', file=sys.stderr)
        return first * second
