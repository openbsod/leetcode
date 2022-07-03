class MyStack:

    def __init__(self):
        self._q = []

    def push(self, x: int) -> None:
        self._q.append(x)
        for _ in range(1, len(self._q)):
            self._q.append(self._q[0])
            self._q.pop(0)

    def pop(self) -> int:
        return self._q.pop(0)

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return not self._q
