import pytest
from coffee_machine import EmptyMachine


class TestHappyPath:
    def test_full_cycle(self) -> None:
        water_filled_machine = EmptyMachine().fill_water()
        beans_loaded_machine = water_filled_machine.load_beans()
        pot_placed_machine = beans_loaded_machine.place_pot()
        brewed_machine = pot_placed_machine.brew()
        result, empty_machine = brewed_machine.pour()
        assert result == "Here's your coffee!"

    def test_two_cycles(self) -> None:
        machine = EmptyMachine()
        machine = machine.fill_water()
        machine = machine.load_beans()
        machine = machine.place_pot()
        machine = machine.brew()
        result, machine = machine.pour()
        # Should be back to EMPTY, ready for another cycle
        machine.fill_water()

class TestInvalidTransitions:
    # Note: in a real code base with static type checking, these tests would not exist.
    # Type violations are caught by mypy before running, not at runtime.

    # λ mypy --strict --allow-redefinition --no-incremental test_coffee_machine.py
    # coffee_machine.py:32: error: "EmptyMachine" has no attribute "brew"  [attr-defined]
    # test_coffee_machine.py:27: error: "EmptyMachine" has no attribute "brew"  [attr-defined]
    # test_coffee_machine.py:33: error: "BeansLoadedMachine" has no attribute "place_cup"; maybe "place_pot"?  [attr-defined]
    # test_coffee_machine.py:40: error: "WaterFilledMachine" has no attribute "fill_water"  [attr-defined]
    # Found 4 errors in 2 files (checked 1 source file)
    def test_cant_brew_when_empty(self) -> None:
        machine = EmptyMachine()
        with pytest.raises(AttributeError):
            machine.brew()

    def test_cant_pour_before_brewing(self) -> None:
        machine = EmptyMachine()
        machine = machine.fill_water()
        machine = machine.load_beans()
        machine = machine.place_pot()
        with pytest.raises(AttributeError):
            machine.pour()


    def test_cant_fill_water_twice(self) -> None:
        machine = EmptyMachine()
        machine = machine.fill_water()
        with pytest.raises(AttributeError):
            machine.fill_water()