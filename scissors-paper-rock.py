#Scissors paper rock
import random
while True:
    print()
    print("1. Scissors")
    print("2. Paper")
    print("3. Rock")
    print("0. Exit")
    choice= input("Enter your choice (0-3): ")
    data= {"1":'Scissors', "2": 'Paper', "3": 'Rock'}
    dataNum=["1","2","3"]
    bot= random.choice(dataNum)
    if choice == bot:
        print("draw")
    elif choice == "0":
        break
    elif choice == "1" and bot == "2":
        print("You won")
    elif choice == "1" and bot == "3":
        print("You lost")
    elif choice == "2" and bot == "1":
        print("You lost")
    elif choice == "2" and bot == "3":
        print("You won")
    elif choice == "3" and bot == "1":
        print("You won")
    elif choice == "3" and bot == "2":
        print("You lost")
    else:
        print("Wrong Input")
    try:
        print("You : "+data[choice])
        print("Bot : "+data[bot])
    except Exception as e:
        print(e)