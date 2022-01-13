# Author: Michael Morriss
# Date: 11/26/2020
# Description: Creates class called AddThreeGame to creates a code game where users take turns entering numbers 1-9
# until 3 of these player's numbers sum to a total of 15, without any repeats.

class BuildersGame:
    """
    Creates class for building game.
    """

    def __init__(self):
        """
        Initializes an empty game board, an unfinished game state, and sets first
        players turn to x's turn.
        """
        self._board = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        self._current_state = "UNFINISHED"
        self._turn = "x"
        self._turn_num = 0
        self._legal = "yes"

        # Coordinates for each player's two builders.
        self._x_build_1 = [0, 0]
        self._x_build_2 = [0, 0]
        self._o_build_1 = [0, 0]
        self._o_build_2 = [0, 0]

    def get_current_state(self):
        """
        Returns the current state of the game, a player win or unfinished.
        """
        return self._current_state

    def initial_placement(self, x_builder_1, y_builder_1, x_builder_2, y_builder_2, player_turn):
        """
        Creates initial placement of player 'x' and player 'o's two builders.
        """
        if self._turn_num >= 2:
            return False

        if player_turn != self._turn:
            return False

        if (x_builder_1 == x_builder_2) and (y_builder_1 == y_builder_2):
            return False

        if x_builder_1 and y_builder_1 and x_builder_2 and y_builder_2 not in range(0, 5):
            return False

        if player_turn == "x":
            self._x_build_1[0] = x_builder_1
            self._x_build_1[1] = y_builder_1

            self._x_build_2[0] = x_builder_2
            self._x_build_2[1] = y_builder_2

            self._turn = "o"
            self._turn_num += 1

            return True

        if player_turn == "o":

            self._o_build_1[0] = x_builder_1
            self._o_build_1[1] = y_builder_1

            self._o_build_2[0] = x_builder_2
            self._o_build_2[1] = y_builder_2

            self._turn = "x"

            # Returns false if o places builders where x has builders.
            if self._turn_num == 1 and ((self._o_build_1[0] == self._x_build_1[0]
                and self._o_build_1[1] == self._x_build_1[1])
                or (self._o_build_1[0] == self._x_build_2[0] and self._o_build_1[1] == self._x_build_2[1])):
                return False

            if self._turn_num == 1 and ((self._o_build_2[0] == self._x_build_1[0]
                and self._o_build_2[1] == self._x_build_1[1])
                or (self._o_build_2[0] == self._x_build_2[0] and self._o_build_2[1] == self._x_build_2[1])):
                return False

            self._turn_num += 1

        return True

    def make_move(self, x_build_from, y_build_from, x_build_to, y_build_to, x_build_up, y_build_up):
        """
        Makes a move for player 'x' or player 'o' by moving one of the current builders one
        adjacent square away (diagonally or orthogonally),
        """
        # Checking if correct player turn, returns false is incorrect turn.
        if (self._turn_num % 2 == 0) and self._turn == "o":
            return False

        if (self._turn_num % 2 == 1) and self._turn == "x":
            return False

        # Checking if numbers are in correct range.
        if (x_build_from or y_build_from or x_build_to or y_build_to or x_build_up or y_build_up) not in range(0, 5):
            return False

        # Checking if move is legal, that is builder's move is adjacent to builder's initial location.
        if y_build_to == y_build_from and (x_build_to == x_build_from + 1 or x_build_to == x_build_from - 1):
            self._legal = "yes"
        elif y_build_to == y_build_from + 1 and (x_build_to == x_build_from + 1 or x_build_to == x_build_from - 1
            or x_build_to == x_build_from):
            self._legal = "yes"
        elif y_build_to == y_build_from - 1 and (x_build_to == x_build_from + 1 or x_build_to == x_build_from - 1
            or x_build_to == x_build_from):
            self._legal = "yes"
        elif (y_build_to != y_build_from) or (y_build_to != y_build_from + 1) or (y_build_to != y_build_from - 1):
            self._legal = "no"

        if self._legal == "no":
            return False

        # Checking if move is legal, that is the building built up is adjacent to builder's most recent position.
        if y_build_up == y_build_to and (x_build_up == x_build_to + 1 or x_build_up == x_build_to - 1):
            self._legal = "yes"
        elif y_build_up == y_build_to + 1 and (x_build_up == x_build_to + 1 or x_build_up == x_build_to - 1
            or x_build_up == x_build_to):
            self._legal = "yes"
        elif y_build_up == y_build_to - 1 and (x_build_up == x_build_to + 1 or x_build_up == x_build_to - 1
            or x_build_up == x_build_to):
            self._legal = "yes"
        elif (y_build_up != y_build_to) or (y_build_up != y_build_to + 1) or (y_build_up != y_build_to - 1):
            self._legal = "no"

        # Returns false if moves are not adjacent.
        if self._legal == "no":
            return False

        # Makes move if player turn is "x" and they are moving their builder 1, and returns false if the
        # player moves to an occupied square, and updates the game state to X_WON if the builder lands
        # on top of a level 3 building.
        if self._turn == "x" and (x_build_from == self._x_build_1[0] and y_build_from == self._x_build_1[1]):
            self._x_build_1[0] = x_build_to
            self._x_build_1[1] = y_build_to
            if (self._x_build_1[0] == self._o_build_1[0]) and (self._x_build_1[1] == self._o_build_1[1]):
                return False
            if (self._x_build_1[0] == self._o_build_2[0]) and (self._x_build_1[1] == self._o_build_2[1]):
                return False
            if (self._x_build_1[0] == self._x_build_2[0]) and (self._x_build_1[1] == self._x_build_2[1]):
                return False
            self._turn = "o"
            self._turn_num += 1
            if self._board[y_build_up][x_build_up] >= 0:
                self._board[y_build_up][x_build_up] += 1
                if self._turn == "x" and self._board[self._x_build_1[1]][self._x_build_1[0]] == 3:
                    self._current_state = "X_WON"
                    return True
            return True

        # Makes move if player turn is "x" and they are moving their builder 2.
        if self._turn == "x" and (x_build_from == self._x_build_2[0] and y_build_from == self._x_build_2[1]):
            self._x_build_2[0] = x_build_to
            self._x_build_2[1] = y_build_to
            if (self._x_build_2[0] == self._o_build_1[0]) and (self._x_build_2[1] == self._o_build_1[1]):
                return False
            if (self._x_build_2[0] == self._o_build_2[0]) and (self._x_build_2[1] == self._o_build_2[1]):
                return False
            if (self._x_build_2[0] == self._x_build_1[0]) and (self._x_build_2[1] == self._x_build_1[1]):
                return False
            self._turn = "o"
            self._turn_num += 1
            if self._board[y_build_up][x_build_up] >= 0:
                self._board[y_build_up][x_build_up] += 1
                if self._turn == "x" and self._board[self._x_build_2[1]][self._x_build_2[0]] == 3:
                    self._current_state = "X_WON"
                    return True
            return True

        # Makes move if player turn is "o" and they are moving their builder 1.
        if self._turn == "o" and (x_build_from == self._o_build_1[0] and y_build_from == self._o_build_1[1]):
            self._o_build_1[0] = x_build_to
            self._o_build_1[1] = y_build_to
            if (self._o_build_1[0] == self._x_build_1[0]) and (self._o_build_1[1] == self._x_build_1[1]):
                return False
            if (self._o_build_1[0] == self._o_build_2[0]) and (self._o_build_1[1] == self._o_build_2[1]):
                return False
            if (self._o_build_1[0] == self._x_build_2[0]) and (self._o_build_1[1] == self._x_build_2[1]):
                return False
            self._turn = "x"
            self._turn_num += 1
            if self._board[y_build_up][x_build_up] >= 0:
                self._board[y_build_up][x_build_up] += 1
                if self._turn == "o" and self._board[self._o_build_1[1]][self._o_build_1[0]] == 3:
                    self._current_state = "O_WON"
                    return True
            return True

        # Makes move if player turn is "o" and they are moving their builder 2
        if self._turn == "o" and (x_build_from == self._o_build_2[0] and y_build_from == self._o_build_2[1]):
            self._o_build_2[0] = x_build_to
            self._o_build_2[1] = y_build_to
            if (self._o_build_2[0] == self._o_build_1[0]) and (self._o_build_2[1] == self._o_build_1[1]):
                return False
            if (self._o_build_2[0] == self._x_build_2[0]) and (self._o_build_2[1] == self._x_build_2[1]):
                return False
            if (self._o_build_2[0] == self._x_build_1[0]) and (self._o_build_2[1] == self._x_build_1[1]):
                return False
            self._turn = "x"
            self._turn_num += 1
            if self._board[y_build_up][x_build_up] >= 0:
                self._board[y_build_up][x_build_up] += 1
                if self._turn == "o" and self._board[self._o_build_2[1]][self._o_build_2[0]] == 3:
                    self._current_state = "O_WON"
                    return True
            return True
