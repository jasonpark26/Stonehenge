"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2 # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move

# TODO: Implement a recursive version of the minimax strategy.


def recursive_minimax(game: Any) -> Any:
    """
    Return a move for game through recursive minimax
    """
    top_move = game.current_state.get_possible_moves()[0]
    available_moves = game.current_state.get_possible_moves()
    game_score = -1
    for moves in available_moves:
        spare = game.current_state.make_move(moves)
        player_score = minimum(spare, game)
        if game.is_over(spare):
            return moves
        elif player_score > game_score:
            top_move = moves
            game_score = player_score
    return top_move


def minimum(gamestate: Any, game: Any) -> Any:
    """
    Helper function for the mini portion of minimax, current player
    """
    available_moves = gamestate.get_possible_moves()
    game_score = 1
    for moves in available_moves:
        spare = gamestate.make_move(moves)
        player_score = maximum(spare, game)
        if player_score < game_score:
            game_score = player_score
    return game_score


def maximum(gamestate: Any, game: Any) -> Any:
    """
    Helper function for the max portion of minimax, other player
    """
    available_moves = gamestate.get_possible_moves()
    game_score = -1
    for moves in available_moves:
        spare = gamestate.make_move(moves)
        player_score = minimum(spare, game)
        if player_score > game_score:
            game_score = player_score
    return game_score


def iterative_minimax(game: Any) -> Any:
    """
    Return a move for game through iterative minimax
    """
    top_move = game.current_state.get_possible_moves()[0]
    available_moves = game.current_state.get_possible_moves()
    game_score = -1
    for moves in available_moves:
        spare = game.current_state.make_move(moves)
        player_score = minimum(spare, game)
        if game.is_over(spare):
            return moves
        elif player_score > game_score:
            top_move = moves
            game_score = player_score
    return top_move


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
