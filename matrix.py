
# after you clone the repo you will see this matrix.

matrix = [
    [True, 34, 5, 'School'],
    [8, 23, 20, 11, 37, 55, 17],
    ['book', 'mosh', 'arc', 'photo'],
    [-1, 'Mani']
]

for num in reversed(matrix[1]):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
              break
        else:
           print(num)


           
for i in matrix[2]:
    print(i.upper())






# You should write a program that do: 
# 1- Find the list that contains ALL STRING and print them on the console on capital letters. 
# For example program will not do anything with first and second array. but the 3rd array contains ALL STRING.
# If an array contains string but there are other data types in array, your program will ignore it.
# So the program will print BOOK MOSH ARC PHOTO
# 2- Find the list that all of its elements are numbers.
# Then print the prime numbers that exists in the list in reverse order.
# During the test I will change the order of matrix. So your program should be able to find the proper array smartly.
# Your prgram should be smart to find the list that contain all strings and all numbers.