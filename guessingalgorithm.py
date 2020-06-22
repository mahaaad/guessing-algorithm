import random

#2d list of the 4 different bags, and what they contain
global bags
bags = [
        ["red","red","red","red","green","green","green","green"], #bag 0
        ["red","red","green","green","green","green","green","green"], #bag 1
        ["red","red","red","red","red","red","green","green"], # bag 2
        ["red","red","red","red","red","red","red","red"], # bag 3
     ]
#list of all the gueses
guesses = []
def main():
    #runs the test n amount of times
    for i in range (0,50000):
        choose()
    correctguesses = 0
    for i in guesses:
        if i == 1:
            correctguesses+=1
    
    print("\n\nThe algorithm guesses with " + str(correctguesses/len(guesses)*100) + "% \aaccuracy")

def choose():
    global bags
    ##empy lists to store data when the you pick 3 the first time, and then the second time
    attemptA = []
    attemptB = []
    print("\n")
    #picks from the 4 bags
    bagNumber = random.randint(0, len(bags)-1)

    print("bag number: " + str(bagNumber))

    if bagNumber == 0:
        print("This bag contains 4 cubes of each colour")
    if bagNumber == 1:
        print("This bag contains 2 red cubes and 6 green cubes")
    if bagNumber == 2:
        print("This bag contains 6 red cubes and 2 green cubes")
    if bagNumber == 3:
        print("This bag contains 8 red cubes")

    for x in range (0,3):
        numcubes = len(bags[bagNumber])-1
        print("numcubes: " + str(numcubes))
        #randomly chooses cube from bag
        randomnum = random.randint(0,numcubes)
        #adds to draw list
        attemptA.append(bags[bagNumber][randomnum])
        #removes the cube from the list so its not chosen twice
        bags[bagNumber].remove(bags[bagNumber][randomnum])

    print("first sample: " + str(attemptA))

    #puts all cubes back in the bag
    bags =  [
        ["red","red","red","red","green","green","green","green"], #bag 0
        ["red","red","green","green","green","green","green","green"], #bag 1
        ["red","red","red","red","red","red","green","green"], # bag 2
        ["red","red","red","red","red","red","red","red"], # bag 3
    ] 

    for x in range (0,3):
        numcubes = len(bags[bagNumber])-1
        print("numcubes: " + str(numcubes))
        #randomly chooses cube from bag
        randomnum = random.randint(0,numcubes)
        #adds to draw list
        attemptB.append(bags[bagNumber][randomnum])
        #removes the cube from the list so its not chosen twice
        bags[bagNumber].remove(bags[bagNumber][randomnum])
        
    
    print("second sample: " + str(attemptB))

    bags =  [
        ["red","red","red","red","green","green","green","green"], #bag 0
        ["red","red","green","green","green","green","green","green"], #bag 1
        ["red","red","red","red","red","red","green","green"], # bag 2
        ["red","red","red","red","red","red","red","red"], # bag 3
    ] 

    #prints guess
    guessNumber = guess(attemptA,attemptB)
    print("\nThe guess would be bag : " + str(guessNumber))
    
    #adds to guess list
    if str(guessNumber) == str(bagNumber):
        guesses.append(1)
    else:
        guesses.append(0)

def guess(attemptA,attemptB):
    redcounta = 0
    greencounta = 0
    redcountb = 0
    greencountb = 0
    for cube in attemptA:
        if cube == "red":
            redcounta+=1
        if cube == "green":
            greencounta+=1

    for cube in attemptB:
        if cube == "red":
            redcountb+=1
        if cube == "green":
            greencountb+=1
    
    print("\nThere are " + str(redcounta) + " red cubes and " + str(greencounta) + " green cubes in the first draw")
    print("There are " + str(redcountb) + " red cubes and " + str(greencountb) + " green cubes in the first draw")

    totalred = redcounta + redcountb
    totalgreen = greencounta + greencountb

    print("There are " + str(totalred) + " red cubes in total")
    print("There are " + str(totalgreen) + " green cubes in total")

    #guess algorithm
    if ((redcounta == 3 and greencountb == 3) or (greencounta == 3 and redcountb == 3)) or totalred == totalgreen:
        #If there are 3 of the same colour, and 3 of the other colour in the next sample then it would be bag 1 (4 green 4 red)
        return 0 #returns index of 1st bag
    
    if totalred < totalgreen:
        # if there are more greens from both samples, it would be bag 2 (6 green 2 red)
        return 1 #returns index of 2nd bag

    if totalred > totalgreen and totalred < 6 :
        #if there's more red but not all red, then its most likely bag 3 (6 red 2 green)
        return 2

    if totalred == 6:
        #if its all red, then it's most likely the bag of all red
        return 3 #returns index of 4th bag
     
main()