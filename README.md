# Coffee Machine Refactoring Kata

## Assignment 
Refactor the `CoffeeMachine` class towards to Typestate pattern. 
This pattern is popular in languages like Rust, but also useful in Python for use cases where you need type safety,
in other words, contexts where it is expensive to accidentally perform an operation to an object in a wrong type state.
See e.g. [implementing typestate pattern in python](https://hackernoon.com/implementing-typestate-pattern-in-python-4u3d34pi)

## Domain
A coffee machine moves through: Empty → WaterFilled → BeansLoaded → CupPlaced → Brewed → Poured (back to Empty). 
Each state only allows the next valid action.

### Detailed explanation
Create a separate class per state, 
each exposing only the valid next method returning the next type (e.g. `EmptyMachine.fill_water() -> WaterFilledMachine`). 
Run your typechecker. Write a valid sequence, you will see that it passes. Write `EmptyMachine().brew()`, confirm the typechecker catches it. 
Done. You've felt the pattern.

The goal is to refactor `coffee_machine.py` so that invalid transitions become typechecker errors instead of runtime exceptions. 
Each state should be its own class, each method should return the next type. 
When you're done, the InvalidStateError and all the guard clauses should be gone.

### How to check your work:

Run `mypy --strict --allow-redefinition coffee_machine.py` (or `pyright` in strict mode)
The happy path script should pass with no type errors
Add a line like `EmptyMachine().brew()` and confirm the typechecker flags it
The tests will need to change too. The TestInvalidTransitions tests no longer make sense as runtime tests. 
Consider replacing them with a small script of "should-fail" lines and verifying mypy/pyright rejects them

Hint: Start by creating `EmptyMachine` with a single method `fill_water() -> WaterFilledMachine`, then work forward one state at a time. 
The pour() method on the final state should return `tuple[str, EmptyMachine]` to close the cycle.




## Type checkers
- mypy: current (May 2026) industry standard
- pyright: slightly faster than mypy
- ty: rust-based from Astral (uv, ruff), very fast. Still in active development. Less aggressive (from the idea that you should not have to add types to working code to pass type checks)
- pyrefly: rust-based from meta, very fast. Still in active development. More aggressive

https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/



## Setup
```bash
uv sync
```
Settings > Add Interpreter > local interpreter > select existing > uv
![img.png](img.png). Uv env use `CoffeeMachine/.venv/Scripts/python.exe`


## Typechecker Setup
Use either mypy (`mypy --strict --allow-redefinition`) or pyright (pyright in strict mode, 
set `"typeCheckingMode": "strict"` in `pyrightconfig.json`). 
Pyright handles variable redefinition out of the box — no extra flag needed. Pick one and stick with it throughout.

