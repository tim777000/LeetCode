class Foo:
    def __init__(self):
        self._first = threading.Lock()
        self._second = threading.Lock()
        self._third = threading.Lock()
        self._second.acquire()
        self._third.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self._first.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._second.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self._second.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self._third.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self._third.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self._first.release()