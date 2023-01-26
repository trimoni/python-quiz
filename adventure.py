name = input('Type your name: ')
print('Welcome', name, 'to this adventure!')

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you ike to go? ").lower()

if answer == 'left':
  answer = input('You come to a river, you can walk around it or swim across? Type to walk around and swim to swim across: ')

  if answer == 'swim':
    print('You swam across and died')
  elif answer == 'walk':
    print('You walked for many miles, died')
  else:
    print('Not a valid option. You suck.')


elif answer == 'right':
  answer == input('You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back) ')

  if answer == 'cross':
    print('You crossed the bridge and lived')
  elif answer == 'back':
    print('You walked back and... died')
  else:
    print('Not a valid option. You suck.')

else:
  print('Not a valid option. You suck.')