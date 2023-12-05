# 0x0A. Prime Game
#### `Algorithm` `Python`

![image](https://github.com/samuelselasi/alx-interview/assets/85158665/e442e69f-f004-4b05-9af0-0186aa323dba)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using `python3` (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version `1.7.x`)
* All your files must be executable

## Tasks

**Maria** and **Ben** are playing a game.
Given a set of consecutive integers starting from `1` up to and including `n`,
they take turns choosing a prime number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round.
Assuming **Maria** always goes first and both players play optimally,
determine who the winner of each game is.

* **Prototype**: `def isWinner(x, nums)`
* where `x` is the number of rounds and `nums` is an array of `n`
* **Return**: `name` of the player that won the most rounds
* If the winner cannot be determined, return `None`
* You can assume `n` and `x` will not be larger than `10000`
* You cannot import any packages in this task

**Example**:
* `x` = `3`, `nums` = `[4, 5, 1]`

### First round: `4`

* **Maria** picks `2` and removes `2`, `4`, leaving `1`, `3`
* **Ben** picks `3` and removes `3`, leaving `1`
* **Ben** wins because there are no *prime numbers* left for **Maria** to choose

### Second round: `5`

* **Maria** picks `2` and removes `2`, `4`, leaving `1`, `3`, `5`
* **Ben** picks `3` and removes `3`, leaving `1`, `5`
* **Maria** picks `5` and removes `5`, leaving `1`
* **Maria** wins because there are no *prime numbers* left for **Ben** to choose

### Third round: `1`

* **Ben** wins because there are no prime numbers for **Maria** to choose

#### Result: Ben has the most wins
```
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
```
```
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
```

# Whiteboarding

## Description


The `Sieve of Eratosthenes` is an ancient algorithm for finding all prime numbers up to a given limit.
It efficiently identifies and eliminates multiples of each prime,
gradually sieving out non-prime numbers until only the primes are left.

Here's a step-by-step explanation of the algorithm:

#### Create a list of integers: 
- Start with a list of integers from `2` to the desired limit. 
  For example, if you want to find all primes up to `30`, your initial list would be 
  `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]`.

#### Start with the first prime:
- The smallest prime number is `2`.
  Mark `2` as prime, and then cross out all multiples of `2` in the list (*excluding 2 itself*).

#### Move to the next number:
- Move to the next number in the list that is not crossed out.
  This is the next prime number.
  Mark it as prime and cross out all multiples of this new prime.

#### Repeat until finished:
- Continue this process, moving to the next non-crossed-out number and marking it as prime,
  while crossing out its multiples.
  Repeat until you've processed all numbers up to the square root of the original limit.

#### Primes remaining:
- After completing the above steps, the remaining numbers in the list that are not crossed out are prime.

The `Sieve of Eratosthenes` is efficient because it avoids redundant work.
When eliminating multiples of a prime, you only need to start crossing out at the square of that prime,
as all smaller multiples would have been crossed out when their smaller prime factors were processed.

For example, when eliminating multiples of `2`, you start crossing out at `4` because `2 * 2` is `4`.
When eliminating multiples of `3`, you start crossing out at `9` because `3 * 3` is `9`, and so on.

This algorithm has a time complexity of `O(n log log n)`,
making it one of the most efficient ways to find all primes within a certain range.

## Pseudocode
function findWinner(totalRounds, roundNumbers):
    if roundNumbers is empty or totalRounds < 1:
        return None

    highestNumber = find the biggest number in roundNumbers
    isPrime = initialize a list of True values from 2 to max(highestNumber + 1, 2)

    // Mark multiples of numbers as not prime
    for i from 2 to square root of highestNumber:
        if isPrime[i] is True:
            for j from i*i to highestNumber, increase by i:
                set isPrime[j] to False

    set isPrime[0] and isPrime[1] to False
    cumulativePrimes = 0

    // Count the number of primes up to each index
    for i from 0 to length of isPrime:
        if isPrime[i] is True:
            cumulativePrimes += 1
        set isPrime[i] to cumulativePrimes

    winner = ''
    player1Score = 0

    // Count how many primes Maria picks
    for n in roundNumbers:
        if isPrime[n] modulo 2 is 1:
            increment player1Score

    // Decide the winner based on the scores
    if player1Score * 2 is equal to length of roundNumbers:
        set winner to None
    if player1Score * 2 > length of roundNumbers:
        set winner to "Maria"
    else:
        set winner to "Ben"

    return winner


