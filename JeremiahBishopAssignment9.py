ghost = 0
hand = ""

##Overload/View Function that is called when the game starts
def playGame():
  ##Initializes the very important Location variable, which is used throughout the game.
  location = "Porch"
  
  ##Shows the text intro.
  showIntroduction()
  
  ##While the player hasn't ended the game, continue it.
  while not (location == "Exit") :
    ##Show the appropriate room.
    ###The Equal Signs are to help better separate the text segments.
    printNow("   ")
    printNow("====================")
    showRoom(location)
    printNow("====================")
    printNow("   ")
    
    ##Ask the player where they want to go next, and show them their selection.
    direction = requestString("Which direction?")
    printNow("You typed: " + direction)
    
    ##Set the location and move the player into the next room.
    ##The direction variable is case insensitive.
    location = pickRoom(direction.lower(), location)
    
## Show the all-text introduction
## Shown at the beginning of the game
def showIntroduction():
  printNow("Welcome to the adventure house!")
  printNow("In each room, you will be told")
  printNow(" which directions you can go.")
  printNow("You can move North, South, East, and West ")
  printNow("by typing that direction.")
  printNow("Type 'help' at any time to replay this introduction.")
  printNow("Type 'quit' or 'exit' to end the program.")
  
##Picks a room based on the direction the player gives it.
##Controlling Function
##Function is called from all rooms
def pickRoom(direction, room): 
  global hand
  
  ##Ends the game, if appropriate
  if(direction == "quit") or (direction == "exit"):
    printNow("Goodbye!")
    return "Exit"
    
  elif(direction == "help"):
    showIntroduction()
    return room
    
    
  elif(room == "Porch"):
    if direction == "north":
      return "Entryway"
  
  elif(room == "Entryway"):
    if direction == "north":
      return "Kitchen"
    elif direction == "east":
      return "LivingRoom"
    elif direction == "south":
      return "Porch"
      
  elif(room == "Kitchen"):
    if direction == "east":
      return "DiningRoom"
    elif direction == "south":
      return "Entryway"
    elif direction == "west":
      return "Attic"
      
  elif(room == "LivingRoom"):
    if direction == "west":
      if hand != "key":
        printNow("That room is locked and unavailable")
        return "LivingRoom"
      else:        
        return "Entryway"
    elif direction == "north":
      return "DiningRoom"
    elif direction == "key":
      hand = "key"
      
  elif(room == "DiningRoom"):
    if direction == "west":
      return "Kitchen"
    elif direction == "south":
      return "LivingRoom"
      
  elif(room == "Attic"):
    if direction == "south":
      return "Kitchen"
 
  printNow("   ")
  printNow("   ")
  printNow("   ")
  printNow("You can't (or don't want to) go in that direction.")
  printNow("   ")
  printNow("   ")
  return room
      
##All of the following show the text for the rooms.

##The Porch
def showPorch():
  printNow("You are on the porch of a frightening looking house.")
  printNow("The windows are broken. It is a dark and stormy night.")
  printNow("You can go north into the house if you dare.")
  
##The Entryway
###Modeling Function
def showEntryway():
  global ghost
  printNow("You are in the entryway of the house.")
  printNow("There are cobwebs in the corner.")
  printNow("You feel a sense of dread.")
  
  if ghost == 0:
    printNow("You suddenly feel cold.")
    printNow("You look up to see a thick mist.")
    printNow("It seems to be moaning; then disappears.")
    ghost = 1
  
  printNow("There is a passageway to the North and another one to the east.")
  printNow("The porch behind you is to the south.")
  
  
## The Kitchen
###Modeling Function
def showKitchen():
  global ghost
  global hand
  
  printNow("You are in the kitchen.")
  printNow("All the surfaces are covered with pots, pans, foodpieces, and pools of blood.")
  printNow("You think you hear something up the stairs that go west")
  printNow("Its a scraping noise, like someone being dragged along the floor")
  
  if ghost == 1:
    printNow("You see the mist you saw earlier.")
    printNow("But now its darker, and red.")
    printNow("The moan increases in pitch and volume.")
    printNow("Now more like a yell.")
    printNow("Then all of a sudden.......")
    printNow("Its gone.")
    ghost = 0
  
  printNow("You can go south or east")
  
  if hand == "key":
    printNow("You have the key, you can go west to go into the attic...")
  
def showLR():
  printNow("You are in the living room.")
  printNow("There are couches, chairs, and small tables")
  printNow("Everything is covered in dust.")
  printNow("You hear a crashing noise in another room.")
  printNow("You can go north or west.")
  
  if hand != "key":
    printNow("There is a key on the other part of the living room.")
    printNow("You can type 'key' to pick it up.")
  
def showDR():
  printNow("You are in the dining room.")
  printNow("There are the remains of a meal.")
  printNow("You can't tell what it is. And maybe don't want to.")
  printNow("Was that a thump to the west?")
  printNow("You can go south or west")
    
def showAttic():
  printNow("You are in the attic.")
  printNow("Everything is quiet.")
  printNow("The room is cluttered with old pictures and cobwebs.")
  printNow("You may travel south back into the kitchen.")
 
##Prints the text part based on the room argument passed through the function  
def showRoom(room):
  if room == "Porch":
    showPorch()
  
  elif room == "Entryway":
   showEntryway()
   
  elif room == "Kitchen":
    showKitchen()
    
  elif room == "LivingRoom":
    showLR()
    
  elif room == "DiningRoom":
    showDR()
    
  elif room == "Attic":
    showAttic()
    
##Starts the game
playGame()