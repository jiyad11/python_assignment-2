
# Question 1 :
# python program to interchange first and last elements in a list.


'''
 my_list = ['apple','kiwi','banana','plums']

temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp

print(my_list)
'''


# Question 2:
# python program to find smallest number in a list

'''
num_list = [50,10,30,3,60,20,5]

smallest_num = num_list[0]

for i in num_list:
    if smallest_num > i:
        smallest_num = i
print(f'{smallest_num} is the smallest number') 

'''


# Question 3:
# write a python program to print Even numbers in a list

'''
myNum_list = [1,2,3,4,5,6,7,8,9,10]

evenNum_list = []

for i in myNum_list:
    if i % 2 == 0:
        evenNum_list.append(i)
print(evenNum_list)

'''

# Question 4:
# write a python program to print Odd numbers in a list

'''
myNum_list = [1,2,3,4,5,6,7,8,9,10]

OddNum_list = []

for i in myNum_list:
    if i % 2 != 0:
        OddNum_list.append(i)
print(OddNum_list)
'''

# Question 5:
# write a python program to print positive numbers  in a list


'''
my_list = [2,-3,4,-6,-9,10]

positiveNum_list = []

for i in my_list:
    if i > 0:
        positiveNum_list.append(i)
print(positiveNum_list)
'''

# Question 6:
# write a python program to print negative numbers  in a list

'''
my_list = [2,-3,4,-6,-9,10]

negativeNum_list = []

for i in my_list:
    if i < 0:
        negativeNum_list.append(i)
print(negativeNum_list)
'''

# Question 7:
# write a python code to convert fahrenheit to celsius

# formula is (100-32)*5/9

'''
fahrenheit = int(input('enter the fahrenheit value: '))

celsius = (fahrenheit - 32) * 5/9
print(celsius)
'''

# Question 8:
# write a python program to print maximum and minimum number in a tuple

'''
my_tuple = (20,10,5,90,100,50,1,8)
my_list = list(my_tuple)

greatest_num = my_list[0]
lowest_num = my_list[0]

for i in my_list:
    if i > greatest_num:
        greatest_num = i
    elif i < lowest_num:
        lowest_num = i

print(greatest_num)
print(lowest_num)
'''

# Question 9:
# write a pyhton program to convert a list into tuple

'''
my_list = [10,20,30,50,70]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
'''

#  Question 10:
# write a python program to create a list and use the following functions: append(),extend(),len()

my_list = [10,30,20,50,100]

my_list2 = [40,60,70,80]

# append
my_list2.append(200)
print(my_list2)

# extend
my_list.extend(my_list2)
myfull_list = my_list
print(myfull_list)

# len function
list_length = len(myfull_list)
print(f'length of the list = {list_length}')
