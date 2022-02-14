# Play with lists/tuples/set using while loops
# - Find maximum from list of ints;
# - Compute the average of tuple items;
# - Reverse list using while loop;
# - Copy items from one list to another;
# - Create new set as union of other two sets, difference of sets and intersection
# Task 1.1
# numbers = [1, 2, 3, 4]
# max_value = max(numbers)
# print("Maximum value: ", max_value)
# Task 1.2
# tuple_items = (1, 2, 3, 4, 5)
# average = sum(tuple_items) / len(tuple_items)
# print("The average of tuple items will be " + str(average))
# Task 1.3
# list1= ['apple', 'banana', 'melon']
# print('Original list:', list1)
# list2=[]
# length=len(list1)
# while length > 0:
# list2.append(list1[length-1])
# length = length - 1
# print('Reversed list:', list2)
# Task 1.4
# list_1 = [1,2,3]
# list_2 = [4,5,6]
# a = list_1
# b = list_2
# a = a + b.copy()
# print (a)
# # Task 1.5
# set_1 = {1, 2,"one", 3}
# set_2 = {"one", 1, 2, "two", "three"}
# a = set_1.union(set_2)
# b = set_1.intersection(set_2)
# print(a)
# print(b)
