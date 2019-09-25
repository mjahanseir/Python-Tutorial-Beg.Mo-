print("Rock...")
print("Paper...")
print("sissors...")

player_1=input("player_1 , make your move : ")
player_2=input("player_2 , make your move : ")

if player_1==player_2 :
    print("that's a tie....")

elif player_1=="rock":
    if player_2=="sissors" :
        print("player_1 wins...")
    elif player_2=="paper":
        print("player_2 wins...")

elif player_1=="paper":
    if player_2=="rock" :
        print("player_1 wins...")
    elif player_2=="sissors":
        print("player_2 wins...")

elif player_1=="sissors":
    if player_2=="paper" :
        print("player_1 wins...")
    elif player_2=="rock":
        print("player_2 wins...")

else:
    print("Sth wrong")