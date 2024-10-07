def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes, starting with box 0
    unlocked_boxes = set([0])
    
    # Create a list to track keys we have found
    keys = set(boxes[0])
    
    # Add keys from the initially unlocked box
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])  # Add new keys from this newly unlocked box
    
    # If the number of unlocked boxes is equal to the total number of boxes, return True
    return len(unlocked_boxes) == len(boxes)



if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
