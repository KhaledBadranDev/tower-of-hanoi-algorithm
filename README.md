# Tower of Hanoi Solver

A Python implementation of the Tower of Hanoi algorithm. This program calculates the steps required to move a stack of disks from a source rod to a target rod, following the standard rules of the puzzle.

![Tower of Hanoi Animation](imgs/tower-of-hanoi.gif)
*Image Source: [freeCodeCamp](https://www.freecodecamp.org/learn/python-v9/lab-tower-of-hanoi/implement-the-tower-of-hanoi-algorithm) (CC-BY-SA 4.0)*

## Description

The `hanoi_solver` function takes an integer `n` (number of disks) and returns a formatted string showing the state of the three rods at every step of the solution.

The algorithm follows these rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No disk may be placed on top of a smaller disk.

## Requirements

* Python 3.x

## Usage

Run the main script to see the output for 3 disks:

```bash
python main.py
```

## License

This project is licensed under the [MIT License](LICENSE).
