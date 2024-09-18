import random
import time

random_number = random.randint(1, 100)
playing = True

while playing:
    guess = int(input("Adivina el número secreto entre 1 y 100. Por favor ingresa un número..."))
    if guess == random_number:
        print("Ganaste!")
        playing = False
    elif guess > random_number:
        print("El número que escogiste es mayor que el número secreto")
    elif guess < random_number:
        print("El número que escogiste es menor que el número secreto \n")
    time.sleep(3) 
    computadora= random.randint(1,100)
    print("la computadora escogió el número...", computadora)
    if computadora == random_number:
        print("La computadora ganó ")
        
        playing = False
    elif computadora > random_number:
        print("El número que la computadora escogió es mayor que el número secreto")
    elif computadora < random_number:
        print("El número que la computadora escogió es menor que el número secreto ")
    