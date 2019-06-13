import random
words = {1: 'india', 2: 'china', 3: 'america', 4: 'canada', 5: 'mexico', 6: 'japan', 7: 'cuba', 8: 'turkey', 9: 'germany', 10: 'paris'}
index = random.randint(1,10)
word = words[index]
word_list = []
for i in range (0, len(word)):
   word_list.append(word[i])
print(word)
guess = []
for i in range(0, len(word_list)):
   guess.append('-')
wrong_turn = 0
while wrong_turn <= 5:
   character = input('Pick a letter: ')

   if character in word_list:
       position = word_list.index(character)
       guess[position] = character
       word_list[position] = '-'
       if '-' not in guess:
           print('You won')
           break # means we found the letter
   else:
       wrong_turn += 1

if wrong_turn >5:
   print('You lose')

print(guess)