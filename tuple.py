filefile = 'filefile.txt'

with open (filefile, 'r' , ) as file:
  lines = file.readlines()

for line in reversed(lines):
    print(line.rstrip('\n'))
