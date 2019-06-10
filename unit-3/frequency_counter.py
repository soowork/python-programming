scores = [5, 15, 25, 7, 7, 15, 25, 67, 8, 5, 3, 5, 7, 5]
# goal -- {5:4, 15:2, 25:2, 7:3, 67:1, 8:1, 3:1}

frequency_counter = {} #empty dictionary

for score in scores:
    if score in frequency_counter:
        frequency_counter[score] += 1
    else:
        frequency_counter[score] = 1

print(f'scores are - {scores}')
print(f'frequency_counter - {frequency_counter}')