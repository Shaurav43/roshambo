import random # for random function
import time # for time function
from os import system, name # for clear screen

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
        # score
        self.score_p1 = 0
        self.score_p2 = 0

    def print_pause(self,message_to_print, sleep_time):
        # change delay time according to sleep_time
        print(message_to_print)
        time.sleep(sleep_time)

    def clear():
        # for windows
        if (name == 'nt'):
            _ = system('cls')
        # for mac and linux
        elif (name == 'posix'):
            _ = system('clear')

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    # ask for rounds
    def TotalRound(self):
        while True:
            self.rounds = input("\n How many rounds would you like to play?\n")
            #checking for an integer number
            if isinstance(self.rounds, int) and self.rounds > 0:
                return self.rounds
            elif self.rounds.lower() == 'exit':
                exit()

    def play_game(self):
        print("Game start!")
        rounds = self.TotalRound()
        for round in range(rounds):
            print(f"\nRound {round + 1}:")
            self.play_round()


    def results(self):
        self.print_pause("Game over!",2)
        self.print_pause(f"\nYour score: {self.score_p1}",2)
        self.print_pause(f"\nComputer's Score: {self.score_p2}\n",2)
        if (self.score_p1>self.score_p2):
            self.print_pause(f"You won by {self.score_p1 - self.score_p2} points")
        else:
            self.print_pause(f"You loss by {self.score_p2 - self.score_p1} points")

    def play_again(self):
        while True:
            ask = input("\n Would you like to play again (Y|N)?").lower()
            if (ask == "y"):
                self.play_game()
            elif (ask =="n"):
                exit()


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
