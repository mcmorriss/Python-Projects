# Author: Michael Morriss
# Date: 2/17/2021
# Description: Program that represents a linked list and offers various functionalities such as insertion and others.

class Node:
    """ A class that acts as a node for the linked list in our application. """

    def __init__(self, data):
        """Initializes the data members for the node class."""
        self._data = data
        self._next = None

    def get_data(self):
        """Returns the current data for the node."""
        return self._data

    def get_next(self):
        """Returns the current next state for the node."""
        return self._next

    def set_data(self, new_data):
        """ Sets data to a new value. """
        self._data = new_data

    def set_next(self, next_val):
        """ Sets next to a new value. """
        self._next = next_val


class LinkedList:
    """ A class that links objects into a list using recursive methods instead of iterative. """

    def __init__(self):
        """ Initializes the head of the linked list to None. """
        self._head = None

    def get_head(self):
        """Returns the current head of the linked list."""
        return self._head

    def set_head(self, new_head):
        """Sets new value to private head variable."""
        self._head = new_head

    def rec_add(self, val, current):
        """Recursive function that acts off the add-helper function."""
        if current.get_next() is None:
            current.set_next(Node(val))
        else:
            current = current.get_next()
            self.rec_add(val, current)

    def add(self, val):
        """ Adds a new value to the linked list. """
        if self._head is None:                          # Adds value if list is empty.
            self._head = Node(val)
        else:
            current = self._head
            self.rec_add(val, current)

    def rec_remove(self, val, previous, current):
        """Recursive function that acts off the remove-helper function using recursion."""
        if current.get_data() is None:                  # Value not found in the list.
            return

        if current.get_data() == val:                   # Value is found, base case.
            previous.set_next(current.get_next())
        else:
            previous = current
            current = current.get_next()
            self.rec_remove(val, previous, current)

    def remove(self, val):
        """Removes a value from the linked list if it matches the parameter value."""
        if self._head is None:                          # Linked list is empty.
            return

        if self._head.get_data() == val:                           # The head is the removable value.
            self._head = self._head.get_next()
        else:
            current = self._head
            previous = None
            self.rec_remove(val, previous, current)

    def rec_contains(self, val, current):
        """Recursive functions that returns True if the value if found, else False is returned."""
        if val == current.get_data():
            is_contains = True
            return is_contains

        if current is None:                   # Value was not found in linked list.
            is_contains = False
            return is_contains
        else:
            current = current.get_next()
            self.rec_contains(val, current)

    def contains(self, val):
        """Returns true if a linked list contains a specific value, returns False if it does not."""
        if self._head is None:                          # If list is empty, returns False.
            return False
        else:
            current = self._head
            self.rec_contains(val, current)
            return True

    def rec_to_plain_list(self, result, current):
        """Recursive function that converts linked list element into a regular list"""
        if current is None:
            return result
        else:
            result.append(current.get_data())
            current = current.get_next()
            self.rec_to_plain_list(result, current)

    def to_plain_list(self):
        """Returns a plain-version of the linked list."""
        if self._head is None:
            return []
        else:
            result = []
            current = self._head
            self.rec_to_plain_list(result, current)
            return result

    def rec_insert(self, val, pos, index, current):
        """Recursive function that inserts parameter value into the parameter position. """
        if current.get_next() is None:                  # Inserts at the end if pos is greater than list length.
            current.set_next(val)
            return

        if pos == index:
            temp = current.get_next()
            current.set_next(Node(val))
            next_one = current.get_next()
            next_one.set_next(temp)
            return
        else:
            index += 1
            current = current.get_next()
            self.rec_insert(val, pos, index, current)

    def insert(self, val, pos):
        """ Inserts a node with a parameter value to a specific parameter position. """
        if self._head is None:  # Inserts value if linked list is empty.
            self.add(val)
            return

        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.set_next(temp)
            return
        else:
            current = self._head
            index = 0
            self.rec_insert(val, pos, index, current)
            return

    def rec_reverse(self, previous, current, following):
        """Recursive function that is executed from the reverse function and reverses the order of a list. """
        if current is None:
            self._head = previous
        else:
            following = current.get_next()
            current.set_next(previous)
            previous = current
            current = following
            self.rec_reverse(previous, current, following)

    def reverse(self):
        """ Reverses the current order of the linked list, without changing any data members of list elements. """
        previous = None
        current = self._head
        following = None
        self.rec_reverse(previous, current, following)