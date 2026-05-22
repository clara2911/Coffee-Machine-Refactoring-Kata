import pytest
from coffee_machine import CoffeeMachine, InvalidStateError


class TestHappyPath:
    def test_full_cycle(self) -> None:
        machine = CoffeeMachine()
        machine.fill_water()
        machine.load_beans()
        machine.place_cup()
        machine.brew()
        result = machine.pour()
        assert result == "Here's your coffee!"

    def test_two_cycles(self) -> None:
        machine = CoffeeMachine()
        machine.fill_water()
        machine.load_beans()
        machine.place_cup()
        machine.brew()
        machine.pour()
        # Should be back to EMPTY, ready for another cycle
        machine.fill_water()


class TestInvalidTransitions:
    def test_cant_brew_when_empty(self) -> None:
        machine = CoffeeMachine()
        with pytest.raises(InvalidStateError):
            machine.brew()

    def test_cant_pour_before_brewing(self) -> None:
        machine = CoffeeMachine()
        machine.fill_water()
        machine.load_beans()
        machine.place_cup()
        with pytest.raises(InvalidStateError):
            machine.pour()

    def test_cant_load_beans_before_water(self) -> None:
        machine = CoffeeMachine()
        with pytest.raises(InvalidStateError):
            machine.load_beans()

    def test_cant_place_cup_before_beans(self) -> None:
        machine = CoffeeMachine()
        machine.fill_water()
        with pytest.raises(InvalidStateError):
            machine.place_cup()

    def test_cant_fill_water_twice(self) -> None:
        machine = CoffeeMachine()
        machine.fill_water()
        with pytest.raises(InvalidStateError):
            machine.fill_water()