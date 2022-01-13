# Author: Michael Morriss
# Date: 11/20/2020
# Description: Creates class called AddThreeGame to creates a code game where users take turns entering numbers 1-9
# until 3 of these player's numbers sum to a total of 15, without any repeats.

class AddThreeGame:
    """
    Creates game that stores data for turns, state, and numbers chosen. Winner
    wins when 3 numbers sum totals to 15.
    """

    def __init__(self):
        """
        Initializes data members for numbers chosen, current game state, and player turn.
        """
        self._numbers = set()
        self._p1_total = []
        self._p2_total = []
        self._current_state = "UNFINISHED"
        self._turn = "first"
        self._turn_num = 0

    def get_current_state(self):
        """
        Returns the current state of the game, either a win, draw, or unfinished.
        """
        return self._current_state

    def make_move(self, player, num_choice):
        """
        Function that allows player 1 or 2 to enter number depending on whose turn it is,
        the number is then added to a list to see if it is the list contains any
        3 numbers that sum to 15 then returns True.
        """
        target = 15
        length_1 = len(self._p1_total)
        length_2 = len(self._p2_total)

        if num_choice in self._numbers or player != self._turn or num_choice not in range(1, 10):
            return False

        if self._current_state != "UNFINISHED":
            return False

        if player == "first":
            self._p1_total.append(num_choice)
            length_1 = len(self._p1_total)

        if player == "second":
            self._p2_total.append(num_choice)
            length_2 = len(self._p2_total)

        if player == "first" and length_1 >= 3:
            for i in range(length_1):
                for j in range(i + 1, length_1):
                    for k in range(j + 1, length_1):
                        if self._p1_total[i] + self._p1_total[j] + self._p1_total[k] == target:
                            self._current_state = "FIRST_WON"
                            return True
            self._p1_total.append(num_choice)
            self._numbers.add(num_choice)
            self._turn = "second"
            return True

        if player == "second" and length_2 >= 3:
            for i in range(length_2):
                for j in range(i + 1, length_2):
                    for k in range(j + 1, length_2):
                        if self._p2_total[i] + self._p2_total[j] + self._p2_total[k] == target:
                            self._current_state = "SECOND_WON"
                            return True
            self._p2_total.append(num_choice)
            self._numbers.add(num_choice)
            self._turn = "first"
            return True

        if player == "first" and length_1 < 3:
            self._numbers.add(num_choice)
            self._turn = "second"
            return True

        if player == "second" and length_2 < 3:
            self._numbers.add(num_choice)
            self._turn = "first"
            return True

        if len(self._numbers) == 9:
            self._current_state = "DRAW"
            return True
