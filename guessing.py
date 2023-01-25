import random

top_of_range = input('Type a number: ')

while True:
  user_guess = input('Make a guess: ')
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Please type a number next time')
    quit()

randum_number = random.randint(0, top_of_range)


