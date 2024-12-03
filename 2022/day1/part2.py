import sys
my_file = open(sys.argv[1], "r")
# reading the file
data = my_file.read()
# replacing end splitting the text 
# when newline ('\n') is seen.
lines = data.split("\n")
t = 0

top = [0,0,0]

for line in lines:
    if line == "":
        if t > min(top):
            top[0] = t
            top.sort()
        t = 0
    else:
        t += int(line)

print(sum(top))
