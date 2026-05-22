# A coffee machine moves through: Empty → WaterFilled → BeansLoaded → PotPlaced → Brewed → Poured (back to Empty).
# Each state only allows the next valid action.

# EmptyMachine with a single method fill_water() -> WaterFilledMachine, then work forward one state at a time.
# The pour() method on the final state should return tuple[str, EmptyMachine] to close the cycle.

class EmptyMachine:
    def fill_water(self) -> "WaterFilledMachine":
        return WaterFilledMachine()

class WaterFilledMachine:
    def load_beans(self) -> "BeansLoadedMachine":
        return BeansLoadedMachine()

class BeansLoadedMachine:
    def place_pot(self) -> "PotPlacedMachine":
        return PotPlacedMachine()

class PotPlacedMachine:
    def brew(self) -> "BrewedMachine":
        return BrewedMachine()

class BrewedMachine:
    def pour(self) -> tuple[str, "EmptyMachine"]:
        return "Here's your coffee!", EmptyMachine()


if __name__ == "__main__":
    # λ mypy --strict --allow-redefinition --no-incremental coffee_machine.py
    # coffee_machine.py:30: error: "EmptyMachine" has no attribute "brew"  [attr-defined]
    coffee_machine = EmptyMachine()
    coffee_machine.brew()
