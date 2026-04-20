import numpy as np 

data	=	np.array([12,	7,	25,	18,	5,	30,	22,	9,	14,	27,	3,	20])

data = data.reshape(3,4) 

print(data)

print("Value at row 2 and col 1 : " , data[1][0])
print("The second row : " , data[2][:])


print("Values greater than 15 : " , data[data > 15])

print("Values between 10 and 25 (inclusive)  : " , data[(data >= 15 ) & (data <= 25)])

print("Sum of all elements : " , np.sum(data))
print("Mean of each row :" , data.mean(axis = 1))
print("Max of each column :" , data.max(axis = 0)) 

value_data = data[data > 10] 

new_data = value_data.reshape(2,-1)

new_data = new_data * 2

print(new_data)



