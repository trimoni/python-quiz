import random

top_of_range = input('Type a number: ')

random_number = random.randint(0, top_of_range)

while True:
  user_guess = input('Make a guess: ')
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Please type a number next time')
    continue

  if user_guess == random_number:
    print('You got it boi!')
  else:
    print('Nope')


