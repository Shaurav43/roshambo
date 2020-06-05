import random  # for random function
import shutil
import time  # for time function
from os import system, name  # for clear screen

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        # learn's the player's move
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer (Player):

    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):

    def move(self):
        if self.their_move:
            return self.their_move
        return self.moves[random.randint(0, 2)]


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
            humanMove = input("rock | paper | scissors ? ").lower()
            if humanMove in self.moves:
                return humanMove
            elif humanMove == 'exit':
                game.end_game()


class Game:

    def __init__(self):
        # score and round initialization
        self.HumanScore = 0
        self.ComputerScore = 0
        self.rounds = 0

    def print_pause(self, message_to_print, sleep_time):
        # change delay time according to sleep_time
        print(message_to_print)
        time.sleep(sleep_time)

    def clear(self):
        # for windows
        if (name == 'nt'):
            _ = system('cls')
        # for mac and linux
        elif (name == 'posix'):
            _ = system('clear')
        column = shutil.get_terminal_size().columns
        print(">>>ROSHAMBO<<<".center(column))
        # print on right side
        if (self.rounds != 'exit' and int(self.rounds) > 0):
            HumanScoreText = ("Your Score: " +
                              str(self.HumanScore)).rjust(column)
            ComputerScoreText = ("Computer: " +
                                 str(self.ComputerScore)).rjust(column)
            print(HumanScoreText + "\n" + ComputerScoreText)
        print("-" * column)

    def intro(self):
        self.print_pause("Welcome To Text Based Rock|Paper|Scissors! Game", 1)
        self.print_pause("To exit during the game please type 'exit'", 2)

    def results(self):
        self.clear()
        self.print_pause("Game over!", 2)
        if (self.HumanScore > self.ComputerScore):
            self.print_pause("You won by " +
                             str(self.HumanScore - self.ComputerScore) +
                             " points", 2)
        elif (self.HumanScore < self.ComputerScore):
            self.print_pause("You loss by " +
                             str(self.ComputerScore - self.HumanScore) +
                             " points", 2)
        else:
            self.print_pause("It was a tie", 2)
        self.play_again()

    def TotalRound(self):
        while True:
            self.rounds = input("How many rounds would you like to play? ")
            # checking for an integer number
            if self.rounds.isdigit() and int(self.rounds) > 0:
                print(self.rounds)
                return self.rounds
            elif self.rounds.lower() == 'exit':
                self.end_game()

    def play_game(self):
        self.clear()
        self.intro()
        self.TotalRound()
        for round in range(int(self.rounds)):
            # random choice in every round
            maingame = MainGame(HumanPlayer(),
                                random.choice([Player(),
                                               RandomPlayer(),
                                               ReflectPlayer(),
                                               CyclePlayer()]))
            self.clear()
            self.print_pause(f"Round {round + 1}:", 2)
            maingame.play_round()
        self.results()

    def play_again(self):
        while True:
            ask = input("Would you like to play again (Y|N)?").lower()
            if (ask == "y"):
                self.play_game()
            elif (ask == "n"):
                self.end_game()

    def end_game(self):
        self.clear()
        self.print_pause("Thank you for playing", 2)
        self.print_pause("Roshambo by Shaurav Thapa", 2)
        exit()


class MainGame:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        game.print_pause(f"\nPlayer 1: {move1}  Player 2: {move2}", 3)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if self.beats(move1, move2):
            game.HumanScore += 1
        elif self.beats(move2, move1):
            game.ComputerScore += 1

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    game = Game()
    game.play_game()
