#Flip a coin
#Check if its heads or tails
#If heads add to list
#If tails add to list
#check if there is a streak of 6 or more in a row

import random
streak = 0
numberOfStreaks = 0
results =[]

#Generate a list of results
for experimentNumber in range(10000):
    for flip in range(100):
        result = random.randint(0, 1)
        if result == 0:
            results.append('H')
        elif result == 1:
            results.append('T')
        if results[flip] == results[flip - 1]:
            streak = streak + 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1
    results = []

print(numberOfStreaks)


print('Chance of streak: %s%%' % (numberOfStreaks / (100*10000)))