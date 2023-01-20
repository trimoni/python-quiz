print('Welcome to my computer quiz')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
  quit()

print("Okay! Let's Play ")
score = 0

answer = input("What color is Ketchup? ")
if answer.lower() == 'red':
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

answer = input("What is the capital of Massachusetts? ")
if answer.lower() == 'boston':
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

answer = input("What stone evolves Pikachu? ")
if answer.lower() == 'thunder stone':
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

answer = input("When did Columbus arrive to America? ")
if answer.lower() == '1492':
  print('Correct!')
  score += 1
else:
  print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "% ")