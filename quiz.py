print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  quit()

print("Okay! Let's Play ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

answer = input("What is the capital of Massachusetts? ")
if answer.lower() == 'boston':
  print('Correct!')
else:
  print('Incorrect!')

answer = input("What stone evolves Pikachu? ")
if answer.lower() == 'thunder stone':
  print('Correct!')
else:
  print('Incorrect!')

answer = input("When did Columbus arrive to America? ")
if answer.lower() == '1492':
  print('Correct!')
else:
  print('Incorrect!')