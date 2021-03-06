from pprint import pprint

def checkChange(instructions):
	j = 0
	alreadyRun = []
	accumulator = 0
	while True:
		thisInstruction = instructions[j][0]
		thisValue = instructions[j][1]
		alreadyRun.append(j)

		# Run the instructions
		if thisInstruction == 'acc':
			accumulator += thisValue
			j += 1
		elif thisInstruction == 'jmp':
			j += thisValue
		else:
			j += 1

		# Check to see if we fixed the boot sequence
		if j in alreadyRun:
			break
		elif j == len(instructions):
			print(accumulator)
			break

# Open and clean up input
rawInstructions = open('input.txt', 'r').read().splitlines()
instructions = [] #each line becomes an item in this list
for i in rawInstructions:
	a = str(i[:3])
	b = int(i[4:])
	instructions.append((a, b)) #each instruction is a list w/2 items

for i in range(len(instructions)):
	newInstructions = instructions.copy()
	thisInstruction = newInstructions[i][0]

	if thisInstruction == 'nop':
		newInstructions[i] = ('jmp', newInstructions[i][1])
	elif thisInstruction == 'jmp':
		newInstructions[i] = ('nop', newInstructions[i][1])
	checkChange(newInstructions)