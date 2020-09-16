from random import randint

answer = randint(1, 100)

while True:
    try:
        
        guess = int(input('Guess a number 1~100:   '))
        if 0 < guess <99:
            if guess == answer:
                print('Your are Genius')
                break
        else:
            print('Hey , I said 1~100')
    except ValueError:
        print("Please enter a Number")



