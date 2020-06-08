import random
import time
from os import system, name

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.my_move = moves
        self.their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class CyclePlayer(Player):

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        for index in range(len(moves) - 1):
            if self.my_move == moves[index]:
                self.my_move = moves[index + 1]
                return self.my_move
        self.my_move = moves[0]
        return self.my_move


class ReflectPlayer(Player):

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if (self.their_move):
            return self.their_move
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        while True:
            move = input("Rock/Paper/Scissors? ").lower()
            if move in moves:
                return move
            elif move == 'exit':
                game.end_game()


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # score initialization
        self.p1_score = 0
        self.p2_score = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def clear(self):
        # clear screen
        # cls for windows
        # clear for mac/linux
        _ = system('cls') if (name == 'nt') else system('clear')

    def print_pause(self, message_to_print, sleep_time):
        # change delay time according to sleep_time
        print(message_to_print)
        time.sleep(sleep_time)

    def intro(self):
        self.print_pause("Welcome To Text Based Rock|Paper|Scissors! Game", 1)
        self.print_pause("To exit during the game please type 'exit'", 2)

    def end_game(self):
        self.display_score()
        self.print_pause("Thank you for playing", 2)
        self.print_pause(" -Roshambo by Shaurav", 2)
        exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        time.sleep(3)
        self.print_pause(f"You: {move1}  Computer: {move2}", 3)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if(self.beats(move1, move2)):
            self.p1_score += 1
        elif(self.beats(move2, move1)):
            self.p2_score += 1

    def display_score(self):
        self.clear()
        print(f"Your Score: {self.p1_score}")
        print(f"  Computer: {self.p2_score}")
        time.sleep(3)

    def play_game(self):
        self.clear()
        self.intro()
        self.print_pause("Game start!", 2)
        rounds = self.total_rounds()
        for round in range(rounds):
            self.display_score()
            self.print_pause(f"Round {round + 1}/{rounds}:", 2)
            self.play_round()
        self.display_score()
        self.print_pause("Game over!", 3)

    def total_rounds(self):
        while True:
            rounds = input("Number of rounds? ")
            if rounds.isdigit() and int(rounds) > 0:
                return int(rounds)
            elif rounds.lower() == 'exit':
                self.end_game()


if __name__ == '__main__':

    play_again = 'y'

    while True:
        game = Game(HumanPlayer(),
                    random.choice([Player(),
                                   RandomPlayer(),
                                   ReflectPlayer(),
                                   CyclePlayer()]))
        if (play_again == 'y'):
            game.play_game()
        play_again = input("Play Again?(Y/N): ").lower()
        if (play_again == 'n'):
            game.end_game()
