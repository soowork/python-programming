'''
# declare an empty list
classmates = []

# add items to list 
classmates.append('Sue')

# output
#   ['Sue']
# print(classmates)

classmates.append('Shad')
classmates.append('Mayank')
classmates.append('Gus')
classmates.append('Chin')
classmates.append('Eva')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Julian')
classmates.append('Aaron')

# Eva
# print(classmates[5])

#   ['Sue', 'Chad']
# print(classmates)

# test = []
# test[0] = 'boo'
# print(test)

# len returns the size of the list 
# print(len(classmates))

# remove last item from list 
# classmates.pop() 
# print(classmates)

# insert at specific position
# classmates.insert(4,'Aaron')
# print(classmates)

# works
# classmates.remove('Gus')
# print(classmates)

# classmates.remove(4)
# print(classmates)

# iterate over list 
# classmate is just a variable that holds a copy of each element of list
# we tend to call it the singular of the list 
# for classmate in classmates:
#     classmates.remove(classmate)

# print(classmate)

# to check each element
# for classmate in classmates:
#     if(classmate == 'Gus'):
#         print('Gus is back!')

# print(classmates)

# enumerate elements
# this gives us
    # 0 Sue
    # 1 Shad
    # 2 Mayank
    # 3 Gus
    # 4 Chin
    # 5 Eva
    # 6 Jeremy
    # 7 Dan
    # 8 Julian
    # 9 Aaron
# for index, classmate in enumerate(classmates):
#     print(index, classmate )

# edit elements while enumerate
# ** enumerate is important as it gives us the index
# for index, classmate in enumerate(classmates):
#     classmates[index] += ' - Python Student'

# print(classmates)


for index, classmate in enumerate(classmates):
    classmates[index] = classmate.upper()
    # this works too 
    #classmates[index] = classmates[index].upper()

print(classmates)

'''
marvel_movies = ['Captain America: The First Avenger','Captain Marvel','Iron Man','Iron Man 2','The Incredible Hulk','Thor','Avengers','Iron Man 3','Thor: The Dark World','Captain America: The Winter Soldier','Guardians of the Galaxy','Guardians of the Galaxy Vol. 2','Avengers: Age of Ultron','Ant-Man','Captain America: Civil War','Spider-Man: Homecoming','Doctor Strange','Black Panther','Thor: Ragnarok','Ant-Man and The Wasp','Avengers Infinity War','Avengers: Endgame']
movies_with_the = []
for movie in marvel_movies:
    if 'the ' in movie.lower():
        #print(movie)
        movies_with_the.append(movie)
        
# print(marvel_movies)
print(movies_with_the)