print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing != 'yes':
  quit()

print("Okay! Let's Play ")

answer = input("What does CPU stand for? ")
if answer == 'central processing unit':
  print('Correct!')