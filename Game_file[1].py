n=29
no_of_guesses=1
print("Number of guesses is limited to only 10 times")
while(no_of_guesses<=10):
    guess_no=int(input("Guess your number:\n"))
    if guess_no<29:
        print("You Guessed Lesser,Please enter higher number\n")
    elif guess_no>29:
        print("You Guessed higher,Please enter lesser number\n")
    else:
        print("You Won, Guessed correctly \n")
        print("you took",no_of_guesses, "guesses to finish")
        break

    print(10-no_of_guesses,"no of guesses left")
    no_of_guesses=no_of_guesses+1

if(no_of_guesses>10):
    print("Game Over")



