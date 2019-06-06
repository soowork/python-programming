#create a function to add any number of integers
def add(*args):
    total = 0 
    for arg in args:
        total += arg
    
    return total

print(add(1,2))
print(add(1,2,3,4,5))
print(add(1,2,7,50,-90,88))
print(add())
print(add(10))