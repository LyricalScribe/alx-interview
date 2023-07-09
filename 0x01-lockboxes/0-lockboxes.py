#!/usr/bin/python3
"""Method to determine lockedboxes"""


def canUnlockAll(boxes):
    unlocked = [0]

    for box_id in range(len(boxes)):
        box = boxes[box_id]

        if len(box) == 0:
            continue
        for key in box:
            if key not in unlocked:
                unlocked.append(key)

    return len(unlocked) == len(boxes)
