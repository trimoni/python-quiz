print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  quit()

print("Okay! Let's Play ")

answer = input("What does CPU stand for? ")
if answer == 'central processing unit':
  print('Correct!')
else:
  print('Incorrect!')

answer = input("What is the capital of Massachusetts? ")
if answer == 'boston':
  print('Correct!')
else:
  print('Incorrect!')

answer = input("What stone evolves Pikachu? ")
if answer == 'thunder stone':
  print('Correct!')
else:
  print('Incorrect!')

answer = input("When did Columbus arrive to America? ")
if answer == '1492':
  print('Correct!')
else:
  print('Incorrect!')