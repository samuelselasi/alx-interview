# 0x05. N Queens
### `Algorithm` `Python`
![1_Zm2pbDR5CS2w2xeUbTBxQQ](https://github.com/samuelselasi/alx-interview/assets/85158665/70227c50-e292-455f-98ef-974d25e7496b)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using `python3` (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version `1.7.*`)
* All your files must be executable

## Tasks

![Judit-photo1_602x433 (1)](https://github.com/samuelselasi/alx-interview/assets/85158665/bcf66020-2431-45fd-a122-cf8f9bedd520)

<sup>Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time</sup>

The **N queens** puzzle is the challenge of placing **N** non-attacking queens on an **N×N** chessboard. Write a program that solves the **N queens** problem.

* **Usage**: `nqueens N`
	* If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
* where `N` must be an integer greater or equal to `4`
	* If `N` is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
	* If `N` is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
* The program should print every possible solution to the problem
	* One solution per line
	* **Format**: *see example*
	* You don’t have to print the solutions in a specific order
* You are only allowed to import the `sys` module

**Read**: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```

## Background

The main goal of the `N-Queens` problem is to determine all possible solutions (or one solution) for a given `N`, which represents the `size` of the chessboard and the number of queens to be placed.
A solution is a configuration of queens on the board where no two queens threaten each other.

The problem is essentially an example of the classic "`backtracking`" algorithm.
The basic idea is to start with an empty board and then place queens one by one, ensuring that no two queens attack each other.
If, at any point, you find that a queen cannot be placed without attacking another, you backtrack and explore other possibilities until a solution is found or all possibilities have been exhausted.

Here's a high-level approach to solving the `N-Queens` problem:

1. Start with an empty `N x N` chessboard.

2. Place a queen in the first row(`a1`) and move to the next row.

3. In the next row, try placing the queen in each column one by one. If a queen can be placed without attacking others, move to the next row.

4. If all columns in the current row have been tried and none of them work, backtrack to the previous row and explore other possibilities.

5. Continue this process until you've successfully placed `N` queens on the board or have explored all possible configurations.

6. Collect and return the valid solutions.

The `N-Queens` problem can be solved using various programming languages and algorithms, such as **recursive backtracking** or **constraint propagation**.
Solving it efficiently for larger `N` values can be quite challenging, and it's a good exercise in problem-solving and algorithm design.
