from enum import Enum, auto


class InvalidStateError(Exception):
    pass


class State(Enum):
    EMPTY = auto()
    WATER_FILLED = auto()
    BEANS_LOADED = auto()
    CUP_PLACED = auto()
    BREWED = auto()


class CoffeeMachine:
    def __init__(self) -> None:
        self.state = State.EMPTY

    def fill_water(self) -> None:
        if self.state != State.EMPTY:
            raise InvalidStateError(f"Can't fill water in state {self.state}")
        self.state = State.WATER_FILLED

    def load_beans(self) -> None:
        if self.state != State.WATER_FILLED:
            raise InvalidStateError(f"Can't load beans in state {self.state}")
        self.state = State.BEANS_LOADED

    def place_cup(self) -> None:
        if self.state != State.BEANS_LOADED:
            raise InvalidStateError(f"Can't place cup in state {self.state}")
        self.state = State.CUP_PLACED

    def brew(self) -> None:
        if self.state != State.CUP_PLACED:
            raise InvalidStateError(f"Can't brew in state {self.state}")
        self.state = State.BREWED

    def pour(self) -> str:
        if self.state != State.BREWED:
            raise InvalidStateError(f"Can't pour in state {self.state}")
        self.state = State.EMPTY
        return "Here's your coffee!"