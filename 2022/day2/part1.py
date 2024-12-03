import sys

opponent_values = {"A":"Rock", "B":"Paper", "C":"Scissors"}
play_values={"Rock":1,"Paper":2,"Scissors":3}
outcome={"win":6,"draw":3,"loss":0}
guess = {"X":"Rock", "Y":"Paper", "Z":"Scissors"}


def eval(opponent, player):
    if opponent == player:
        return outcome["draw"] 
    if opponent == "Rock":
        if player == "Paper":
            return outcome["win"]
        else:
            return outcome["loss"]
    if opponent == "Scissors":
        if player == "Rock":
            return outcome["win"]
        else:
            return outcome["loss"]
    if opponent == "Paper":
        if player == "Scissors":
            return outcome["win"]
        else:
            return outcome["loss"]



input_file = open(sys.argv[1], "r")
# reading the file
data = input_file.read()

lines = data.split("\n")
total = 0

for line in lines:
    plays = line.split(" ")
    opponent_move = opponent_values[plays[0]]
    player_move = guess[plays[1]]
    total += eval(opponent_move,player_move) + play_values[player_move]

print(total)
input_file.close()