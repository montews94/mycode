#!/usr/bin/python3
import sys
import os
import random

def showInstructions():
  #print a main menu and the commands
    print('''
RPG Game
You upset a powerful wizard, and he responded by locking you inside your own mind.
You need to find a way to escape!
=================================================================================
Commands:

go [north, east, south,
west, outside, or inside]
get [item]
use [item]
''')

def showStatus():
  #print the player's current status
    print('---------------------------')

    print('You are at the ' + currentRoom)
    #let user know there is a character!
    if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
        print("Oh no, there's a bear inside the cabin!")
    if 'character' in rooms[currentRoom] and 'wizard' in rooms[currentRoom]['character']:
        print("""The Wizard is Spying on you from the Castle Ruins! He sees you
and hurls hurls a spell right at you!...""")
    if 'character' in rooms[currentRoom] and 'enchantress' in rooms[currentRoom]['character']:
        print("There is an Enchantress in the mansion")
  #print the current inventory
    print('You have: ' + str(inventory) + ' in inventory')
  #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + ' on the floor')
        print("---------------------------")

# we need to define the different uses of items in different locations
def itemsUse():
    if move[1] == 'bottle':
        showStatus()
        global currentRoom
        if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
            print("You throw the bottle and it shatters! It scares the bear giving youjust enough time to escape!")
            inventory.remove("bottle")
            currentRoom = 'Cabin'
    if move[1] == 'mirror':
        showStatus()
        if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
            print("you throw the mirror and it shatters! It scares the bear giving you just enough time to escape")
            inventory.remove("mirror")
            currentRoom = 'Cabin'
        if 'character' in rooms[currentRoom] and 'wizard' in rooms[currentRoom]['character']:
            print("""You draw your mirror and reflect the wizards attack! The Wizard dodges
and disappears...""")
            #remove wizard from castle by deleting key pair
            del rooms[currentRoom]['character']

#an inventory, which is initially empty
inventory = []

#a dictionary linking locations
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
                  'character' : 'enchantress',
               },
               'Cabin' : {
                  'north' : 'West End Bridge',
                  'east'  : 'Lake',
                  'south'  : 'Woods',
                  'inside' : 'Cabin Front Room',
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
                  'inside' : 'Castle Ruins Courtyard',
            },
            'East End Bridge' : {
                  'east' : 'Castle Ruins',
                  'west' : 'West End Bridge',
                  'item' : 'key'
                  },
            'Cabin Front Room' : {
                    'character' : 'bear',
                    'outside' : 'Cabin',
            },
            'Castle Ruins Courtyard' : {
                    'character' : 'wizard',
                    'outside' : 'Castle Ruins',
                    },
         }
#start the player in the Hippocampus( where dreams are formed)
currentRoom = 'Hippocampus'

#clear the screen so game is the only thin being displayed
os.system('clear')
#give instructions to player in the beginning of the game
showInstructions()

#loop until win/loss criteria are met
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
  # get key is returned ["get",  "key"]          
    move = move.lower().split(" ", 1)
    #clear the screens previous moves
    os.system('clear')
  #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
      #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new location
        else:
            print('You can\'t go that way!')

  #if they type 'get' first
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
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
    #if item is not in inventory to use
    if move[0] == 'use' :
        if move[1] in inventory:
            #check items usages from function
            itemsUse()
            #otherwise, the item is no in the inventory list
        else:
            #print can not use:
            print('Can\'t use ' + move[1] + '! Not in inventory!')


  ## players primary objective
    if currentRoom == 'Brick Wall' and 'key' in inventory:
        showStatus()
        print("You managed to reach the Brick Wall with the key. You see a door magically appear, and you enter the key. As soon as you turn handle and open the door you wake up... YOU WIN!")
        break

  ## If a player enters a room with a character and loses
    if 'character' in rooms[currentRoom] and 'bear' in rooms[currentRoom]['character']:
        if "mirror" not in inventory and "bottle" not in inventory:
            #give the player 50/50 odds of escaping without items
            bear_attack = random.randint(0,1)
            if bear_attack == 0 :
                showStatus()
                print("The bear attacks you and you die... Game Over!")
                break

    if 'character' in rooms[currentRoom] and 'wizard' in rooms[currentRoom]['character']:
        if "mirror" not in inventory:
            #give player 25% chance of escaping
            wizard_attack = random.randint(0,4)
            if wizard_attack != 0 :
                showStatus()
                print("""You were turned to stone and can no longer escape... GAME OVER!""")
                break
