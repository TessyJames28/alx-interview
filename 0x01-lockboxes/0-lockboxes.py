#!/usr/bin/python3
""" Function that determines if all the boxes can be opened """


def canUnlockAll(boxes):
    """ Check if all boxes can unlock """
    n = len(boxes)
    unlocked_boxes = [0]  # initialize with the index of the first box
    collected_keys = []

    for box in unlocked_boxes:
        keys = boxes[box]  # get keys in the current boxes

        for key in keys:
            if key not in collected_keys:  # check and append new keys
                collected_keys.append(key)

                if key < n and key not in unlocked_boxes:  # check valid box k
                    unlocked_boxes.append(key)  # add new boxes to unlocked box

    return len(unlocked_boxes) == n
