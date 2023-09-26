# 0x00. Pascal's Triangle
#### `Algorithm` `Python`
![Pascals-Triangle](https://github.com/samuelselasi/alx-interview/assets/85158665/08af0d5b-4dfd-4a73-a76a-f06dc3a29063)

## Concepts
### Pascal's Triangle
## Task

[0. Pascal's Triangle](./0-pascal_triangle.py)

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer
```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$
```

# Whiteboarding

1. Function - `pascal_triangle(n)`
2. Initialize an empty list to store Pascal's Triangle - `triangle = []`
3. Check if `n` is less than or equal to zero and return an empty list
4. Loop from `1` to `n` to store the current row in a new list = `row = []`
5. Under the previous loop, loop through the current row elements and if the current is the first or last element set it to `1` - `row.append(1)`
6. If not the first or last element, calculate the element by summing the 2 from the previous row and add it to the list - `row.append(element)`
7. Add the current `row` to the `triangle` - `triangle.appemd(row)`
8. Return the triangle
