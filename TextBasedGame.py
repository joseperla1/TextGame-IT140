#Jose Perla

#Sample function showing the goal of the game and move commands
def show_instructions():
   #print a main menu and the commands
   print("Redemption of a failed Knight Game")
   print('You awaken from your most recent defeat from the Dark Wizard.You see your home was taken over by the enemy, you must reclaim your home')
   print('First you have to improve your magic by finding your magic staff and the three elemental runes, and gear up with a sword and armor')
   print('After you have become stronger head back to the castle to defeat your foe. You must redeem your honor')
   print("Collect 6 items to win the game, or beaten by the Dark Wizard.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")

   print('------------------------------------------')

#Adictionary linking a room to other rooms

def main():
   rooms = {
      'Forest Clearing' : { 'South' : 'Forest', 'North': 'The Great Bridge', 'East' : 'BlackSmith', 'West' : 'Old Shack' },
      'Forest' : { 'North' : 'Forest Clearing', 'East' : 'Riverbank', 'item' : 'Earthrune' },
      'Riverbank' : { 'West' : 'Forest', 'item' : 'Waterrune' },
      'BlackSmith' : { 'West' : 'Forest Clearing', 'North' : 'Home' , 'item' : 'Sword' } ,
      'Home' : {'South' : 'BlackSmith' , 'item' : 'Armor'},
      'Old Shack' : {'East' : 'Forest Clearing' , 'item' : 'Firerune'},
      'The Great Bridge' : {'South' : 'Forest Clearing' , 'East' : 'Castle' , 'item' : 'Magicstaff'},
      'Castle' : {'West' : 'The Great Bridge' , 'Boss' : 'Dark Wizard'} #villain
   }
# status that will show the room, inventory and item in room during gameplay
   def showStatus():
       print('------------------------------------------')
       print('You are in : {}.'.format(currentRoom))
       print('inventory : {}.'.format(inventory))
       if 'item' in rooms[currentRoom].keys():
           nearby_item = rooms[currentRoom]['item']
           if nearby_item not in inventory:
               print(f'You see {nearby_item}')
       print('------------------------------------------')
       #assigning values to current room and inventory
   currentRoom = 'Forest Clearing'
   inventory = []

   show_instructions()
   while True:
       showStatus()

    #Winning Condition
       if 'Boss' in rooms[currentRoom].keys():
           if len(inventory) == 6:
               print('With your newfound power you gather elemental energy to your magic staff and blast the Dark Wizard.You won your rematch against the Dark Wizard Congrats!!')
               break
           #losing condition
           else:
               print("You were too weak, your magic could not rival that of your enemy, you lost your rematch with the Dark Wizard")
               break

       player_entry = input('Enter your move:')
       next_move = player_entry.split(' ')
       player_move = next_move[0].title()
       item='item'
       movement = 'null'
       if len(next_move) > 1:
           item = next_move[1:]
           movement = next_move[1].title()
           item = ' '.join(item).title()

       # how player movement will be done
       if player_move =='Go':
          try:
              currentRoom=rooms[currentRoom][movement]
          except:
              print('Oops Wrong Way')
       #how player will get item
       elif player_move == 'Get':
           try:
               if item == rooms[currentRoom]['item']:
                   if item not in inventory:
                       inventory.append(rooms[currentRoom]['item'])
                   else:
                       print('You already have this item')
               else:
                   print('Cant find that item here')
           except:
               print('Cant find that item here')

      #how player will exit the game
       elif player_move == 'exit':
           print('Goodbye exiting game...')
           break
       else:
           print('Invalid Entry')

main()