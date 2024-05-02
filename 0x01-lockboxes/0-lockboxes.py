def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)
        keys = boxes[current_box]
        for key in keys:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
