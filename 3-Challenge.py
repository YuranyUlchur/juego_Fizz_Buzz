#!/usr/bin/python3
print("you have to write the numbers from 1 to 100 but you have 3 conditions")
print("For each number divisible by three the computer will display the word “fizz”")

score = 0
vida = 3

for i in range(1, 101):
    
    if i % 15 == 0:
        user_input = input("Enter the number: ")
        if user_input != "Fizz-Buzz":
            print("Wrong input. Game Over.")
            vida = vida -1
            if vida == 0:
                break
    elif i % 3 == 0:
        user_input = input("Enter the number: ")
        if user_input != "Fizz":
            print("Wrong input. Game Over.")
            vida = vida -1
            print(vida)
            if vida == 0:
                break
    elif i % 5 == 0:
        user_input = input("Enter the number: ")
        if user_input != "Buzz":
            print("Wrong input. Game Over.")
            vida = vida -1
            print(vida)
            if vida == 0:
                break
    else:
        user_input = input("Enter the number: ")
        if user_input != str(i):
            print("Wrong input. Game Over.")
            vida = vida -1
            print(vida)
            if vida == 0:
                break
    score += 10

print("Final score: ", score)
