class Hiker:

    def answer(self: Hiker, first: int, second: int) -> int:
        # The learner put a print inside a loop to see what was happening.
        # behave holds a step's output back and prints all of it when the step
        # fails, ahead of the summary, so the summary is what the runner's 50K
        # cap on stdout drops.
        total = 0
        for i in range(5000):
            print(f'debug: i is {i}, total is {total}')
            total += 1
        return first * second
