import sys

opponent_values = {"A":"Rock", "B":"Paper", "C":"Scissors"}
play_values={"Rock":1,"Paper":2,"Scissors":3}
outcome={"win":6,"draw":3,"loss":0}
wanted_outcomes={"Z":"win", "Y":"draw", "X":"loss"}
win_move = {"Rock":"Paper", "Scissors":"Rock","Paper":"Scissors"}
loss_move = {"Paper":"Rock", "Rock":"Scissors","Scissors":"Paper"}

def eval(opponent, wanted_outcome):
    if wanted_outcome == "draw":
        return opponent
    if wanted_outcome == "win":
        return win_move[opponent]
    if wanted_outcome == "loss":
        return loss_move[opponent]

input_file = open(sys.argv[1], "r")
# reading the file
data = input_file.read()

lines = data.split("\n")
total = 0

for line in lines:
    plays = line.split(" ")
    opponent_move = opponent_values[plays[0]]
    wanted_outcome = wanted_outcomes[plays[1]]
    total += outcome[wanted_outcome] + play_values[eval(opponent_move,wanted_outcome)]

print(total)
input_file.close()