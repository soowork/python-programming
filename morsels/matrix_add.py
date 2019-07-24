matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

#add(matrix1, matrix2)
#[[3, -3], [-3, 3]]

print('matrix[0]: ', matrix1[0])
print('matrix[0][0]: ', matrix1[0][0])


# lists
    # len(list)
    # list[0] == first element
    # list.append(item)
    # list.insert(index,item)
    # list.pop(<optional_index>) -- removes
    # for item in colletion:
        # do stuff


num_lists = len(matrix1)
sum_list = [None]*num_lists
list_pos = []

for l in range(num_lists):
    list_pos = matrix1[l]
    num_elem = len(list_pos)-1
    for i in range(num_elem):
        print( matrix1[l][i] )
        print( matrix2[l][i] )
        sum_list[l][i] = matrix1[l][i] + matrix2[l][i]


print( 'matrix1: ',matrix1)
print( 'matrix2: ',matrix2)
print( 'result: ',sum_list)
