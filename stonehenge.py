"""
An implementation of Stonehenge.

"""
from typing import Any
import copy
from game_state import GameState
from game import Game


"Implement classes StonehengeGame (subclass of Game) and StonehengeState " \
"(subclass of GameState) to implement the game Stonehenge, and save " \
"them in stonehenge.py."


class StonhengeGame(Game):
    """
    Abstract class for a game to be played with two players for Stonehenge
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        """
        side = int(input("Enter the number of sides: "))
        self.current_state = StonehengeState(p1_starts, side)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        return "Players take turns claiming cells (in the diagram: circles " \
               "labelled with a capital letter). When a player captures at " \
               "least half of the cells in a ley-line (in the diagram: " \
               "hexagons with a line connecting it to cells), then the " \
               "player captures that ley-line. The First player to capture " \
               "at least half of the ley-lines is the winner.A ley-line, " \
               "once claimed, cannot be taken by the other player."

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        one_occ = 0
        two_occ = 0
        leylines = int((3 * state.sides) + 3)
        for leys in state.current_hedge:
            one_occ += state.current_hedge[leys][-1].count('1')
            two_occ += state.current_hedge[leys][-1].count('2')
        if one_occ >= (leylines / 2):
            return True
        elif two_occ >= (leylines / 2):
            return True
        return False
        # if the p1 or p2 has the majority of the hedges then it is over

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))
        # return whether the player has the majority of the hedges
        # used from the given subtract square

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        if not string.strip().isalpha():
            return -1

        return string.upper().strip()


class StonehengeState(GameState):

    """
    The state of a game at a certain point in time for Stonehenge.
    """

    def __init__(self, is_p1_turn: bool, sides: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        super().__init__(is_p1_turn)
        self.sides = sides
        if self.sides == 1:
            self.current_hedge = {'-': [['A', 'B'], ['C'], ['@', '@']],
                                  '/': [['A'], ['B', 'C'], ['@', '@']],
                                  '\\': [['A', 'C'], ['B'], ['@', '@']]}
        elif self.sides == 2:
            self.current_hedge = {'-': [['A', 'B'], ['C', 'D', 'E'], ['F', 'G'],
                                        ['@', '@', '@']],
                                  '/': [['A', 'C'], ['B', 'D', 'F'], ['E', 'G'],
                                        ['@', '@', '@']],
                                  '\\': [['C', 'F'], ['A', 'D', 'G'],
                                         ['B', 'E'], ['@', '@', '@']]}
        elif self.sides == 3:
            self.current_hedge = {'-': [['A', 'B'], ['C', 'D', 'E'],
                                        ['F', 'G', 'H', 'I'], ['J', 'K', 'L'],
                                        ['@', '@', '@', '@']],
                                  '/': [['A', 'C', 'F'], ['B', 'D', 'G', 'J'],
                                        ['E', 'H', 'K'], ['I', 'L'],
                                        ['@', '@', '@', '@']],
                                  '\\': [['F', 'J'], ['C', 'G', 'K'],
                                         ['A', 'D', 'H', 'L'], ['B', 'E', 'I'],
                                         ['@', '@', '@', '@']]}
        elif self.sides == 4:
            self.current_hedge = {'-': [['A', 'B'], ['C', 'D', 'E'],
                                        ['F', 'G', 'H', 'I'],
                                        ['J', 'K', 'L', 'M', 'N'],
                                        ['O', 'P', 'Q', 'R'],
                                        ['@', '@', '@', '@', '@']],
                                  '/': [['A', 'C', 'F', 'J'],
                                        ['B', 'D', 'G', 'K', 'O'],
                                        ['E', 'H', 'L', 'P'], ['I', 'M', 'Q'],
                                        ['N', 'R'], ['@', '@', '@', '@', '@']],
                                  '\\': [['J', 'O'], ['F', 'K', 'P'],
                                         ['C', 'G', 'L', 'Q'],
                                         ['A', 'D', 'H', 'M', 'R'],
                                         ['B', 'E', 'I', 'N'],
                                         ['@', '@', '@', '@', '@']]}
        elif self.sides == 5:
            self.current_hedge = {'-': [['A', 'B'], ['C', 'D', 'E'],
                                        ['F', 'G', 'H', 'I'],
                                        ['J', 'K', 'L', 'M', 'N'],
                                        ['O', 'P', 'Q', 'R', 'S', 'T'],
                                        ['U', 'V', 'W', 'X', 'Y'],
                                        ['@', '@', '@', '@', '@', '@']],
                                  '/': [['A', 'C', 'F', 'J', 'O'],
                                        ['B', 'D', 'G', 'K', 'P', 'U'],
                                        ['E', 'H', 'L', 'Q', 'V'],
                                        ['I', 'M', 'R', 'W'],
                                        ['N', 'S', 'X'],
                                        ['T', 'Y'],
                                        ['@', '@', '@', '@', '@', '@']],
                                  '\\': [['O', 'U'], ['J', 'P', 'V'],
                                         ['F', 'K', 'Q', 'W'],
                                         ['C', 'G', 'L', 'R', 'X'],
                                         ['A', 'D', 'H', 'M', 'S', 'Y'],
                                         ['B', 'E', 'I', 'N', 'T'],
                                         ['@', '@', '@', '@', '@', '@']]}

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        if self.sides == 1:
            return "      {}   {}\n" \
                   "     /   / \n" \
                   "{} - {} - {}\n" \
                   "     \\ / \\\n" \
                   "  {} - {}   {}\n" \
                   "       \\\n" \
                   "        {}\n"\
                .format(self.current_hedge['/'][2][0],
                        self.current_hedge['/'][2][1],
                        self.current_hedge['-'][2][0],
                        self.current_hedge['-'][0][0],
                        self.current_hedge['-'][0][1],
                        self.current_hedge['-'][2][1],
                        self.current_hedge['-'][1][0],
                        self.current_hedge['\\'][2][1],
                        self.current_hedge['\\'][2][0])

        elif self.sides == 2:
            return "        {}   {}\n" \
                   "       /   /\n" \
                   "  {} - {} - {}   {}\n" \
                   "     / \\ / \\ /\n" \
                   "{} - {} - {} - {}\n" \
                   "     \\ / \\ / \\ \n" \
                   "  {} - {} - {}   {}\n" \
                   "       \\   \\ \n" \
                   "        {}   {}\n "\
                .format(self.current_hedge['/'][-1][0],
                        self.current_hedge['/'][-1][1],
                        self.current_hedge['-'][-1][0],
                        self.current_hedge['-'][0][0],
                        self.current_hedge['-'][0][1],
                        self.current_hedge['/'][-1][2],
                        self.current_hedge['-'][-1][1],
                        self.current_hedge['-'][1][0],
                        self.current_hedge['-'][1][1],
                        self.current_hedge['-'][1][2],
                        self.current_hedge['-'][-1][2],
                        self.current_hedge['-'][2][0],
                        self.current_hedge['-'][2][1],
                        self.current_hedge['\\'][-1][2],
                        self.current_hedge['\\'][-1][0],
                        self.current_hedge['\\'][-1][1])

        elif self.sides == 3:
            return "          {}   {}\n" \
                   "         /   /\n" \
                   "    {} - {} - {}   {}\n" \
                   "       / \\ / \\ /\n" \
                   "  {} - {} - {} - {}   {}\n" \
                   "     / \\ / \\ / \\ /\n" \
                   "{} - {} - {} - {} - {}\n" \
                   "     \\ / \\ / \\ / \\ \n " \
                   " {} - {} – {} - {}   {}\n" \
                   "       \\   \\   \\ \n" \
                   "        {}   {}   {} \n"\
                .format(self.current_hedge['/'][-1][0],
                        self.current_hedge['/'][-1][1],
                        self.current_hedge['-'][-1][0],
                        self.current_hedge['-'][0][0],
                        self.current_hedge['-'][0][1],
                        self.current_hedge['/'][-1][2],
                        self.current_hedge['-'][-1][1],
                        self.current_hedge['-'][1][0],
                        self.current_hedge['-'][1][1],
                        self.current_hedge['-'][1][2],
                        self.current_hedge['/'][-1][3],
                        self.current_hedge['-'][-1][2],
                        self.current_hedge['-'][2][0],
                        self.current_hedge['-'][2][1],
                        self.current_hedge['-'][2][2],
                        self.current_hedge['-'][2][3],
                        self.current_hedge['-'][-1][3],
                        self.current_hedge['-'][3][0],
                        self.current_hedge['-'][3][1],
                        self.current_hedge['-'][3][2],
                        self.current_hedge['\\'][-1][3],
                        self.current_hedge['\\'][-1][0],
                        self.current_hedge['\\'][-1][1],
                        self.current_hedge['\\'][-1][2])

        elif self.sides == 4:
            return "            {}   {}\n" \
                   "           /   /\n" \
                   "      {} - {} - {}   {}\n" \
                   "         / \\ / \\ /\n" \
                   "    {} - {} - {} - {}   {}\n" \
                   "       / \\ / \\ / \\ /\n" \
                   "  {} - {} - {} - {} – {}   {} \n" \
                   "     / \\ / \\ / \\ / \\ / \n" \
                   "{} - {} - {} - {} - {} - {} \n" \
                   "     \\ / \\ / \\ / \\ / \\ \n" \
                   "  {} - {} – {} - {} – {}   {} \n" \
                   "       \\   \\   \\   \\ \n" \
                   "        {}   {}   {}   {} \n"\
                .format(self.current_hedge['/'][-1][0],
                        self.current_hedge['/'][-1][1],
                        self.current_hedge['-'][-1][0],
                        self.current_hedge['-'][0][0],
                        self.current_hedge['-'][0][1],
                        self.current_hedge['/'][-1][2],
                        self.current_hedge['-'][-1][1],
                        self.current_hedge['-'][1][0],
                        self.current_hedge['-'][1][1],
                        self.current_hedge['-'][1][2],
                        self.current_hedge['/'][-1][3],
                        self.current_hedge['-'][-1][2],
                        self.current_hedge['-'][2][0],
                        self.current_hedge['-'][2][1],
                        self.current_hedge['-'][2][2],
                        self.current_hedge['-'][2][3],
                        self.current_hedge['/'][-1][4],
                        self.current_hedge['-'][-1][3],
                        self.current_hedge['-'][3][0],
                        self.current_hedge['-'][3][1],
                        self.current_hedge['-'][3][2],
                        self.current_hedge['-'][3][3],
                        self.current_hedge['-'][3][4],
                        self.current_hedge['-'][-1][4],
                        self.current_hedge['-'][4][0],
                        self.current_hedge['-'][4][1],
                        self.current_hedge['-'][4][2],
                        self.current_hedge['-'][4][3],
                        self.current_hedge['\\'][-1][4],
                        self.current_hedge['\\'][-1][0],
                        self.current_hedge['\\'][-1][1],
                        self.current_hedge['\\'][-1][2],
                        self.current_hedge['\\'][-1][3])

        elif self.sides == 5:
            return "              {}   {}\n" \
                   "             /   /\n" \
                   "        {} - {} - {}   {}\n" \
                   "           / \\ / \\ /\n" \
                   "      {} - {} - {} - {}   {}\n" \
                   "         / \\ / \\ / \\ /\n" \
                   "    {} - {} - {} - {} – {}   {} \n" \
                   "       / \\ / \\ / \\ / \\ / \n" \
                   "  {} - {} - {} - {} - {} - {}   {}\n" \
                   "     / \\ / \\ / \\ / \\ / \\ / \n" \
                   "{} - {} - {} - {} - {} - {} - {}  \n" \
                   "     \\ / \\ / \\ / \\ / \\ / \\  \n" \
                   "  {} - {} - {} - {} - {} - {}   {} \n" \
                   "       \\   \\   \\   \\   \\ \n" \
                   "        {}   {}   {}   {}   {} \n"\
                .format(self.current_hedge['/'][-1][0],
                        self.current_hedge['/'][-1][1],
                        self.current_hedge['-'][-1][0],
                        self.current_hedge['-'][0][0],
                        self.current_hedge['-'][0][1],
                        self.current_hedge['/'][-1][2],
                        self.current_hedge['-'][-1][1],
                        self.current_hedge['-'][1][0],
                        self.current_hedge['-'][1][1],
                        self.current_hedge['-'][1][2],
                        self.current_hedge['/'][-1][3],
                        self.current_hedge['-'][-1][2],
                        self.current_hedge['-'][2][0],
                        self.current_hedge['-'][2][1],
                        self.current_hedge['-'][2][2],
                        self.current_hedge['-'][2][3],
                        self.current_hedge['/'][-1][4],
                        self.current_hedge['-'][-1][3],
                        self.current_hedge['-'][3][0],
                        self.current_hedge['-'][3][1],
                        self.current_hedge['-'][3][2],
                        self.current_hedge['-'][3][3],
                        self.current_hedge['-'][3][4],
                        self.current_hedge['/'][-1][5],
                        self.current_hedge['-'][-1][4],
                        self.current_hedge['-'][4][0],
                        self.current_hedge['-'][4][1],
                        self.current_hedge['-'][4][2],
                        self.current_hedge['-'][4][3],
                        self.current_hedge['-'][4][4],
                        self.current_hedge['-'][4][5],
                        self.current_hedge['-'][-1][5],
                        self.current_hedge['-'][5][0],
                        self.current_hedge['-'][5][1],
                        self.current_hedge['-'][5][2],
                        self.current_hedge['-'][5][3],
                        self.current_hedge['-'][5][4],
                        self.current_hedge['\\'][-1][5],
                        self.current_hedge['\\'][-1][0],
                        self.current_hedge['\\'][-1][1],
                        self.current_hedge['\\'][-1][2],
                        self.current_hedge['\\'][-1][3],
                        self.current_hedge['\\'][-1][4])
        return ''

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> state = StonehengeState(True, 1)
        >>> state.get_possible_moves()
        ['A', 'B', 'C']
        >>> state = StonehengeState(True, 2)
        >>> state.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        """
        one_occ = 0
        two_occ = 0
        leylines = int((3 * self.sides) + 3)
        for leys in self.current_hedge:
            one_occ += self.current_hedge[leys][-1].count('1')
            two_occ += self.current_hedge[leys][-1].count('2')
        if one_occ >= (leylines / 2):
            return []
        elif two_occ >= (leylines / 2):
            return []
        moves = []
        for leys in self.current_hedge:
            for lists in self.current_hedge[leys]:
                for letter in lists:
                    if letter.isalpha() is True:
                        moves.append(letter)
        good_moves = list(set(moves))
        good_moves.sort()
        return good_moves

    def make_move(self, move: Any) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        """

        new_state = copy.deepcopy(self)

        for leys in new_state.current_hedge:
            for lines in new_state.current_hedge[leys]:
                for i in range(len(lines)):
                    if lines[i] == move:
                        if self.p1_turn is True:
                            lines[i] = '1'
                        elif self.p1_turn is False:
                            lines[i] = '2'
        for leys in new_state.current_hedge:
            for i in range(len(new_state.current_hedge[leys]) - 1):
                if new_state.current_hedge[leys][i].count('1') >= \
                        (len(new_state.current_hedge[leys][i]) / 2) and \
                        new_state.current_hedge[leys][-1][i] != '2':
                    new_state.current_hedge[leys][-1][i] = '1'
                elif new_state.current_hedge[leys][i].count('2') >= \
                        (len(new_state.current_hedge[leys][i]) / 2) and \
                        new_state.current_hedge[leys][-1][i] != '1':
                    new_state.current_hedge[leys][-1][i] = '2'
        if new_state.p1_turn is True:
            new_state.p1_turn = False
        elif new_state.p1_turn is False:
            new_state.p1_turn = True
        return new_state

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).

        >>> state = StonehengeState(True, 1)
        >>> state.__repr__()
        "P1's Turn: True - P1's Leylines 0 - P2's Leylines 0 - LeyLines Left: 6"
        >>> state = StonehengeState(True, 2)
        >>> state.__repr__()
        "P1's Turn: True - P1's Leylines 0 - P2's Leylines 0 - LeyLines Left: 9"
        """
        one_occ = 0
        two_occ = 0
        leylines = int((3 * self.sides) + 3)
        leys_left = (leylines - one_occ - two_occ)
        for leys in self.current_hedge:
            one_occ += self.current_hedge[leys][-1].count('1')
            two_occ += self.current_hedge[leys][-1].count('2')
        return "P1's Turn: {} - P1's Leylines {} - P2's Leylines {} " \
               "- LeyLines Left: {}"\
            .format(self.p1_turn, one_occ, two_occ, leys_left)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.

        >>> state = StonehengeState(True, 1)
        >>> state.rough_outcome()
        1
        """
        scores = [self.make_move(j) for j in self.get_possible_moves()]
        p11 = []
        scores_1 = []
        for moves in scores:
            p11.append(moves.over())
        for othermoves in scores:
            scores_1.append([self.make_move(k)
                             for k in othermoves.get_possible_moves()])
        for othermoves1 in scores_1:
            for k in othermoves1:
                k.over()
        if True in p11:
            return self.WIN
        elif (True in u for u in scores_1):
            return self.LOSE
        return self.DRAW

    def over(self) -> bool:
        """
        Return whether or not this game is over at state.
        """
        one_occ = 0
        two_occ = 0
        leylines = int((3 * self.sides) + 3)
        for leys in self.current_hedge:
            one_occ += self.current_hedge[leys][-1].count('1')
            two_occ += self.current_hedge[leys][-1].count('2')
        if one_occ >= (leylines / 2):
            return True
        elif two_occ >= (leylines / 2):
            return True
        return False


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
