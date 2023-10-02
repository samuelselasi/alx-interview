#!/usr/bin/python3
"""Module to determine if a list of boxes contain keys to other boxes"""


def canUnlockAll(boxes):
    """Function to determine keys from list of boxes"""

    def dfs(box_index, visited):
        """Function to implement Depth-First Search algorithm"""

        visited[box_index] = True

        # Iterate through the key(s) in the current box
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key, visited)

    num_boxes = len(boxes)

    # Track visited boxes
    visited = [False] * num_boxes

    # Start DFS from the first box (index[0])
    dfs(0, visited)

    return all(visited)
