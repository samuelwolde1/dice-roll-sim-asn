import random

loop = True

def roll2Dice():
    rand1 = random.randrange(1, 7)
    rand2 = random.randrange(1, 7)
    
    print(str(rand1) + "," + str(rand2) + ' (Sum: ' + str(rand1 + rand2) + ')')
    return rand1 + rand2

while loop == True:
    print("\nDice Roll Simulator Menu")
    print('1. Roll Dice Once')
    print('2. Roll Dice 5 Times')
    print('3. Roll Dice \'n\' times')
    print('4. Roll Dice untill Snake Eyes')
    print('5. Exit')
    selection = input('Select an option (1-5): ')

    if selection == "1":
        roll2Dice()

    elif selection == "2":
        for number in range(5):
            roll2Dice()

    elif selection == "3":
        n = input('How many rolls would you like? ')
        for number in range(int(n)):
            roll2Dice()
    
    elif selection == "4":
        for n in range(rand1 + rand2)
        while loop3 == True:
            roll2Dice()
            rolls+=1
            if sum == 2:
                print('You got snake eyes')

                
            
            

