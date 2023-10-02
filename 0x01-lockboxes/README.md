# 0x01. Lockboxes
#### `Algorithm` `Python`

![a2ca62cd87e0](https://github.com/samuelselasi/alx-interview/assets/85158665/35d7c515-9ae0-46e6-972d-961f27e6d94b)

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu `20.04` LTS using python3 (version `3.4.3`)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be documented
* Your code should use the `PEP 8` style (version `1.7.x`)
* All your files must be executable

## Tasks

[0. Lockboxes](./0-lockboxes.py)

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A `key` with the same number as a box opens that box
* You can assume all keys will be positive integers
	* There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```
```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```

## Background

```
In the "Lockboxes" problem, the primary data structure used is a list of lists,
where each inner list represents a lockbox containing keys to other lockboxes.
The problem revolves around determining if all the boxes can be opened starting from the first box.
While the problem itself doesn't require advanced data structures or algorithms,
there are some fundamental concepts at play:
```

1. **Lists** (***Arrays***): `Lists` (or *arrays*) are used to represent the `lockboxes` and their contents.
Each list element represents a lockbox, and the contents of each lockbox are stored as elements within these lists.

2. **Graph Traversal** ([DFS](https://www.askpython.com/python/examples/depth-first-search-algorithm) or [BFS](https://www.askpython.com/python/examples/breadth-first-search-graph)): The core algorithmic concept in this problem is `graph traversal`. The lockboxes and their keys can be seen as `nodes` and edges in a graph.
You need to determine if there's a path from the first box to all other boxes. 
This can be accomplished using either `Depth-First Search (DFS)` or `Breadth-First Search (BFS)` algorithms to traverse the graph.

3. **Visited Flags**: To keep track of which boxes have been visited during the traversal, a `list` (or array) of `boolean values`, often referred to as "*visited flags*", is used.
Each element in this list corresponds to a box, and it is marked as `True` when the box is visited and `False` when it's not.

4. **Recursion** (*in some implementations*): Some solutions use recursive functions to traverse the graph.
In these implementations, a function is called recursively to explore each box's keys and continue the traversal.

5. **Loops Detection** (*in advanced implementations*): In more advanced versions of the problem,
you might need to implement a `loop detection mechanism` to handle cases where there are `circular dependencies` among the boxes.
This requires more complex algorithms and data structures like `sets` or `dictionaries` to detect loops.
