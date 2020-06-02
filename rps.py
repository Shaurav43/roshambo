import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""
class Player:
    moves = ['rock', 'paper', 'scissors']
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        # learn's the player's move
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

# random player
class RandomPlayer (Player):
    def move(self):
        return random.choice(self.moves)

# reflects the player's last move
class ReflectPlayer(Player):
    def move(self):
        return self.their_move
# cycles player's move
class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]

class HumanPlayer(Player):
    def move(self):
        while True:
            humanMove = input("\nrock | paper | scissors ?\n").lower()
            if humanMove in self.moves:
                return humanMove
            elif humanMove == 'exit':
                exit()
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
