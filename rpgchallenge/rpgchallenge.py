#!/usr/bin/python3
import sys
import os

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
    print('''
RPG Game
You upset a powerful wizard, and he responded by locking you inside your own mind.
You need to find a way to escape!
=================================================================================
Commands:

go [north, east, south, or west]
get [item]
''')

def showStatus():
  #print the player's current status
    print('---------------------------')

    print('You are at the ' + currentRoom)
  #print the current inventory
    print('You have: ' + str(inventory) + ' in inventory')
  #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + ' on the floor')
        print("---------------------------")
    if 'character' in rooms[currentRoom] and 'wizard' in rooms[currentRoom]['character']:
        print("The Wizard is in the castle ruins")
    if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
        print("There is a bear hehind the cabin")
    
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hippocampus' : {
                  'north' : 'Woods',
                  'east'  : 'Rolling Mountains',
                  'west'  : 'Corn Fields',
                },

            'Woods' : {
                  'north' : 'Cabin',
                  'south' : 'Hippocampus',
                  'item'  : 'bottle',
                },
            'Rolling Mountains' : {
                  'north' : 'Lake',
                  'west' : 'Hippocampus',
                  'item' : 'mirror',
               },
            'Corn Fields' : {
                  'north' : 'Mansion',
                  'east' : 'Hippocampus',
                  'item' : 'ring',
               },
            'Mansion' : {
                  'east' : 'Brick Wall',
                  'south' : 'Corn Fields',
               },
               'Cabin' : {
                  'north' : 'West End Bridge',
                  'east'  : 'Lake',
                  'south'  : 'Woods',
                  'character' : 'bear',
                },

            'Lake' : {
                  'north' : 'Castle Ruins',
                  'south' : 'Rolling Mountains',
                  'west'  : 'Cabin',
                },
            'Brick Wall' : {
                  'south' : 'West End Bridge',
                  'west' : 'Mansion',
               },
            'West End Bridge' : {
                  'north' : 'Brick Wall',
                  'east' : 'East End Bridge',
                  'south' : 'Cabin',
               },
            'Castle Ruins' : {
                  'south' : 'Lake',
                  'west' : 'East End Bridge',
                  'character' : 'wizard',
            },
            'East End Bridge' : {
                  'east' : 'Castle Ruins',
                  'west' : 'West End Bridge',
                  'item' : 'key'
            }
         }
#start the player in the Hall
currentRoom = 'Hippocampus'

os.system('clear')

showInstructions()

#loop forever
while True:

    showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
    move = ''
    while move == '':
        move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    os.system('clear')
  #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
      #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

  #if they type 'get' first
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to g
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
            inventory.append(move[1])
      #display a helpful message
            print('You got the ' + move[1])
      #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to ge
        else:
      #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

  ## Define how a player can win
    if currentRoom == 'Brick Wall' and 'key' in inventory:
        showStatus()
        print("You managed to reach the Brick Wall with the key. You see a door magically appear, and you enter the key. As soon as you turn handle and open the door you wake up... YOU WIN!")
        break

  ## If a player enters a room with a monster
    if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
        if "miror" not in inventory and "bottle" not in inventory:
            showStatus()
            print("The bear jumps out from behind the cabin and Attacks you... Game Over!")
            break
        if "bottle" in inventory:
            showStatus()
            print("You throw the bottle and it shatters! It's enough to scare the bear, and it  runs away.")
            del rooms[currentRoom]['character']
            inventory.remove("bottle")
        elif "mirror" in inventory:
            showStatus()
            print("You throw the mirror and it shatters! Startled, the bear runs away.")
            del rooms[currentRoom]['character']
            inventory.remove("mirror")
    if 'character' in rooms[currentRoom] and 'wizard' in rooms[currentRoom]['character']:
        if "mirror" in inventory:
            showStatus()
            print("The wizard is using the castle ruins to spy inside your mind, and sees you're looking for a way out. Enraged, he hurls a spell at you! You quickly draw the mirror and reflect the wizard's spell turning him to stone! you suddenly ragain conciousness... YOU WIN!")
            break
        showStatus()
        print("The Wizard is using the castle ruins to spy inside your mind, and sees you're looking for a way out. Enraged, he hurls a spell at you! You are now trapped in stone and unable to escape... GAME OVER!")
        break
