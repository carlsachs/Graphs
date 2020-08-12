# Add up and print the sum of the all of the minimum elements of each inner array:
list1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
#4 + -1 + 9 + -56 + 201 + 18 = 175

list2 = []

#Set it to list
#Grab each inner array with a for loop 
#grab minimum in that set
#create new list
#set minimum value to that list
#add up list
#print

for item in list1:
    list2.append(min(item))

print(sum(list2))
