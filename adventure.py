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
  print()
else:
  print('Not a valid option. You suck.')