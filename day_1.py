# Advent of Code 2022 - Day One
# Get the sum of the top K elves calories
def topKMostCalories(n):
    mostCalories = [0 for i in range(n)]
    _min = 0
    _max = 0

    with open('inputs/day-1.txt', 'r') as calsInput:
        lines = calsInput.readlines()

    runningTotal = 0
    for line in lines:
        if len(line.strip()) == 0: # Empty lines dictate a new elf
            if runningTotal > _min or runningTotal < _max:
                mostCalories.append(runningTotal)
            
                print(mostCalories)
                # Sort the added input
                mostCalories.sort(reverse=True)
                print(mostCalories)


                # Remove the old minimum
                if len(mostCalories) > n:
                    mostCalories.pop(-1)

            runningTotal = 0
        else:
            runningTotal += int(line)

    return sum(mostCalories)

if __name__ == '__main__':
    answer = topKMostCalories(3)
    
    print("Day one solution: ", answer)
        
