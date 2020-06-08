import random

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
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class CyclePlayer(Player):
    def move(self):
        for index in range(len(moves) - 1):
            if self.my_move == moves[index]:
                self.my_move = moves[index + 1]
                return self.my_move
        self.my_move = moves[0]
        return self.my_move

class ReflectPlayer(Player):
    def move(self):
        if (self.their_move):
            # self.my_move = self.their_move
            # return self.my_move
            return self.their_move
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Please type Rock/Paper/Scissors: ")
            if move in moves:
                return move



class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        rounds = self.total_rounds()
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")

    def total_rounds(self):
        while True:
            rounds = input("Please enter total number of rounds you want to play: ")
            if rounds.isdigit() and int(rounds) > 0:
                return int(rounds)
            elif rounds.lower() == 'exit':
                self.end_game()

    def end_game(self):
        print("Thank you for playing")
        print(" -Roshambo by Shaurav")
        exit()


if __name__ == '__main__':
    play_again = 'y'
    while True:
        game = Game(HumanPlayer(),
                    random.choice([ Player(),
                                    RandomPlayer(),
                                    ReflectPlayer(),
                                    CyclePlayer()]))
        if (play_again == 'y'):
            game.play_game()
        play_again = input("Play Again?(Y/N): ").lower()
        if (play_again == 'n'):
            game.end_game()