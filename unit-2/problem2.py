num = 5
num_list = [1,3,5,7,11,13]

print("BEFORE")
print(num_list)
print("num = ",num)

for index, element in enumerate(num_list):
    num_list[index] = element * num 

print("AFTER")
print(num_list)


