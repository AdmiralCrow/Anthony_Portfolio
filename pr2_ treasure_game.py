print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("Welcome traveler!\n You have been trusted with finding the worlds most powerful ring, a ring that is said to rule all of mankind. A ring that has somehow been forgotten through time, you have been given a map with where the ring was last mentioned in historic documents. You must find it before mankinds enemies do!\n")
print("As you begin your travels you reach a forest that goes by the name of Murk Wood. As you enter the Murk Wood you notice the trees are huge and prevent much of the sunlight to touch the forest floor.\n")
cross_road = input(print("As you follow a marked path on the map for some time you reach a Y in the road, one that is not mentioned in your map. Which direction do you choose Left or Right? "))
cross_road = cross_road.lower()


if cross_road == "left":
    print("You take the left path following the road, and after some time begin to hear birds chirping and the sound of singing and splashing. You check the map and see the Great Lake of Ozof is coming up. After what seemed like forever you finally reach the edge of the forst and peaking though some bushes you notice beautiful water spirits dancing and singing in the water. One spots you and waves for you to join them to enter the water and splash with them.\n")
    to_swim = input(print(" Will you join them? Swim or Wait"))
    to_swim = to_swim.lower()
    if to_swim == "wait":
        print("You wait and continue to watch from the bushes, the spirits hiss at you for not falling for their trap. They dive and disappear into the water. Some time passes and as the sun falls into slumber the moon rises for its night shift, when all of a sudden a glowing path appears on the map showing a hidden sandy path through the water, you fallow this path for a few hours. When you finlly reach a 3 doors floating above the water. A Blue, Red and Yellow door.")
        door = input(print("Which door do you choose? Red, Blue, Yellow"))
        door = door.lower()
        if door == "yellow":
            print(" you open the yellow door by pushing it forward and you step into a dark plain, as you enter lights begin to illuminate a path leading to a stone hand grasping something that you cant see from so far. You begin to walk forward and reach the shining object to realize it is the ring you where charged with finding.\n YOU WIN")
        elif door == "red":
            print(" As you push open the red door you feel your hand get hotter, to the point that it begins to blister from the heat of the door. as you step back and see the dark void behind the door a small light appears at the end, but it grows faster and faster to which you realize a gient fireball shoots through the door and straight into you.\n GAME OVER")
        else:
            print("You push open the blue door and see what looks like the bottom of the ocean on the other side. You stick your head through the door only to see a tenticle grab you and drag you in through the door. The door closes.\n GAME OVER")
    else:
        print("You begin to undress yourself and proceed to run and then dive into the water makeing a big splash, But as you surface you hear nothing, no singing, no dancing spirts, just dead silence. When all of a sudden you feel somthing nip at you. You look down and see a trout currently pulling at a bit of your belly flabs. You attempt to smack it away when another bites you in the back, than another and another. When you least expected it you were swarmed by trout and they begin to feast into your flesh. you gasp for air find not oxygen but water filling your lungs.\n GAME OVER ")
else:
    print(" You take the right and follow the road, but after sometime you notice the forest becomes darker and darker to the point you cannot see where forward begins and backwards ends. You contine to walk in the darkness never to be heard of again.\n GAME OVER")

