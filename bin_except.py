# Author: Michael Morriss
# Date: 1/24/2021
# Description:  The code below provides a modified binary search function that is similar to the binary search
# function that was exhibited in the course exploration 4; however, this modified version raises a
# custom user exception called TargetNotFound when a target element is not present in a user list.


class TargetNotFound(Exception):
    """
    User exception created to raise an error in the binary search function when the target value
    is not found in the user list.
    """
    pass


def bin_except(some_list, target):
    """
    Uses binary search algorithm to search for a target value within a list, if value is found then the
    index of the value is returned, else an error, TargetNotFound error, is raised.
    """
    first = 0
    last = len(some_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if some_list[middle] == target:
            return middle
        if some_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound
