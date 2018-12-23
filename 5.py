def isReactable(polymer, i):
    return abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32

def reacts(polymer, i):
    polymer = polymer[:i] + polymer[i + 2:]
    return polymer
polymer = input().strip()

i = 0
iteration = 0
while i < len(polymer) - 1:
    if iteration % 1000 == 0:
        print(iteration)
    if isReactable(polymer, i):
        polymer = reacts(polymer, i)
        i -= 1
        if i < 0:
            i = 0
    else:
        i += 1
    iteration += 1
        
print("Remaining length of Polymer: ", len(polymer))
