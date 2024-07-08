import random

moves = ['rock', 'paper', 'scissors']

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        while True:
            if RandomPlayer(my_move, their_move) == move2


class ReflectPlayer(Player):
    def learn():
        


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    

class Human_player(Player):
    def move(self):
        while True:
            try:
                choice_ = input("Rock, paper, scissors? ")
                choice_.lower()
                if choice_ != "rock" and choice_ != "paper" and choice_ != "scissors":
                    raise ValueError()
                return choice_
            except ValueError as e:
                print("Invalid input")
                continue 


class Game:
    def __init__(self, Human_player, p2):
        self.Human_player = Human_player
        self.p2 = p2

    @staticmethod
    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.Human_player.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.Human_player.learn(move1, move2)
        self.p2.learn(move2, move1)

        if self.beats(move1, move2):
            print("Player 1 wins!")
        elif self.beats(move2, move1):
            print("Player 2 wins!")
        else:
            print("It's a tie!")

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

if __name__ == '__main__':
    game = Game(Human_player(), RandomPlayer())
    game.play_game()


"""5. Create player classes that remember
At the end of each game round, the Game class calls the learn method on each player object, to tell that player what the other player's move was. This means you can have computer players that change their moves depending on what has happened earlier in the game. To do this, you will need to implement learn methods that save information into instance variables.

Create a ReflectPlayer class that remembers what move the opponent played last round, and plays that move this round. (In other words, if you play 'paper' on the first round, a ReflectPlayer will play 'paper' on the second round.)

Create a CyclePlayer class that remembers what move it played last round, and cycles through the different moves. (If it played 'rock' this round, it should play 'paper' in the next round.)

(Something to think about: What should these classes do on the first move?)"""



# Round 0 --
# Rock, paper, scissors? > rock
# You played rock.
# Opponent played paper.
# ** PLAYER TWO WINS **
# Score: Player One 0, Player Two 1

# Round 1 --
# Rock, paper, scissors? > 