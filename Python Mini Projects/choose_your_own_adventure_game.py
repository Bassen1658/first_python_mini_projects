name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
answer = input("You are on a dirt road, it had com to an end and you can go left or right. which way would you like to go? left/right ").lower()
if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross it. swim/walk ").lower()
    
    if answer == "swim":
        print("You were eaten by an alligator and lost the game!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game!")
    else:
        print("Not a valid answer, you loose!")
        

elif answer == "right":
    answer = input("You have arrived to an old bridge. It seems kinda wobbly, but there is not another bridge for miles. Do you cross or walk around? cross/walk ").lower()
    if answer == "cross":
        print("The bridge collapses and you lost the game!")
    elif answer == "walk":
        answer = input("You walked for many miles, and finaly found a way across the river. On the other side an old man is waiting for you. Do you talk to him or do you try to sneek past? talk/sneek ").lower()
        if answer == "talk":
            print("The old man greets you as the king of the vale and you live happy ever after! ")
        elif answer == "sneek":
            print("You try to sneek past but slips on a stone and dies, and therfore lose the game! ")
        else:
            print("Not a valid answer, you loose!")
    else:
        print("Not a valid answer, you loose!")
else:
    print("Not a valid answer, you loose!")

print("Thank you for playing!")