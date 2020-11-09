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

died = "You died. Game over"
badResponse = "Wrong choice! this aint minecraft. You dont have free will. "
moveDirection = input("Do you want to move left or right?\n")

if moveDirection == "left":
  print(died)
elif moveDirection == "right":
  swimOrWait = input("You come across a river. Do you want to swim or wait?\n")
  if swimOrWait == "swim":
    print("You got eaten by crocs. " + died)
  elif swimOrWait == "wait":
    print("A boat came and ferried you across. You now come across a door")
    whichDoor = input("Which door will you open, rock, metal or wood\n")
    if whichDoor == "metal":
      print("Metal door... on an adventure game.. naaah " + died)
    elif whichDoor == "rock":
      print("A door made of rock?? You dumbass. " + died)
    elif whichDoor == "wood":
      print("The wooden door opens and you enter a great hall")
      stealTrophy = input("There's a golden trophy on a counter, will you take it? yes or no\n")
      if stealTrophy == "yes":
        print("Its never a good idea to steal stuff on an adventure game " + died)
      elif stealTrophy == "no":
        print("Well, that was easy! Success on your win.")
      else:
        print(badResponse)
    else:
      print(badResponse)
  else:
    print(badResponse)
else: 
  print(badResponse)
