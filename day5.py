# --- day 5: thermal vents! --- 
# Authors: Vj and TheAvrgAvocado

with open ("input5.txt", "r") as input:
  cmds = input.read().split("\n")

print(len(cmds))

inputLines = []

def ifMatching(x1, y1, x2, y2):
  if x1 == x2 and y1 == y2:
    return True
  else:
    return False

while True:
    try: 
        a, b, c, d = map(int, input5().replace(",", " ").split())
        inputLines.append([(a, b), (c,d)])
    except ValueError:
        break

print(inputLines)