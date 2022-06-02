import random

opt = {
    "R" : "Rock",
    "P" : "Paper",
    "S" : "Scissors"
}
possible_opt = []
for i in opt:
    possible_opt += i    
    
is_on = True

while is_on:

    comp_choice = random.choice(possible_opt)

    players_choice = input("'R' for rock, 'P' for paper, 'S' for scissors: \n").upper()

    
    if players_choice in possible_opt:
        
        print(f"Player({opt[players_choice]}) : CPU({opt[comp_choice]})")
        
        if players_choice == "R" and comp_choice == "S":
            print("player wins")
            is_on = False
        elif players_choice == "P" and comp_choice == "R":
            print("player wins")
            is_on = False
            
        elif players_choice == "S" and comp_choice == "P":
            print("player wins")
            is_on = False
            
        elif players_choice == comp_choice:
            print("it's a tie")
        else:
            print("CPU wins")
            is_on = False
    else:
        print("Error. Invalid Entry, try again")
            