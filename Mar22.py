# Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.

# def print_down_from_n(n:int):
#     if n <= 0:
#         return
#     print(n)
#     print_down_from_n(n - 1)

# print_down_from_n(5)


# Write a function print_characters(s) that prints each character of a string on a new line using recursion.

# def print_characters(s:str):
#     if not s:  
#         return
#     print(s[0])  
#     print_characters(s[1:])

# print_characters("hello")



# Write a recursive function to calculate the factorial of a number n.

# def factorial(n:int)->int:
#     if n <= 0:  
#         return 1
#     return n * factorial(n - 1) 


# print(factorial(5)) 

# Create a recursive function to find the sum of the first n natural numbers.
# The sum of natural numbers from 1 to n is calculated by adding all the numbers in the range. For example, the sum of the first 4 numbers is 1 + 2 + 3 + 4 = 10.

# def sum_natural(n:int) -> int:
#     if n == 0:
#         return 0
#     return n + sum_natural(n - 1) 


# print(sum_natural(10))  


#  Fibonacci Sequence
# Write a recursive function to calculate the nth Fibonacci number.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. For example, the sequence begins as 0, 1, 1, 2, 3, 5, 8....

# def fibonacci(n):
#     if n == 0:  
#         return 0
#     if n == 1:  
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)  


# print(fibonacci(6)) 

# Write a recursive function to reverse a given string.
# Reversing a string means rearranging its characters from the last to the first.
# For example, the string "hello" becomes "olleh".

# def reverse_string(s:str)->str:
#     if len(s) == 0:  
#         return ""
#     return s[-1] + reverse_string(s[:-1])

# print(reverse_string("world"))  


# Write a recursive function to check if a string is a palindrome.
# A palindrome is a string that reads the same backward as forward. For example, "madam" is a palindrome, but "hello" is not.

# def is_palindrome(s:str)->bool:
#     if len(s) <= 1:  
#         return True
#     if s[0] != s[-1]:  
#         return False
#     return is_palindrome(s[1:-1])  

# print(is_palindrome("level"))
# print(is_palindrome("hello"))   


# Write a recursive function to calculate the power of a number x raised to n.
# For example, 2^4 means multiplying 2 by itself 4 times: 2 * 2 * 2 * 2 = 16.


# def power(x, n):
#     if n == 0:  
#         return 1
#     return x * power(x, n - 1)  


# print(power(3, 3))  

# Write a recursive function to calculate the sum of all digits in a number.
# For example, the digits of 1234 add up to 1 + 2 + 3 + 4 = 10.


# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_of_digits(n // 10)  


# print(sum_of_digits(456))  

# Write a recursive binary search algorithm to find the index of a target value in a sorted array.
# Binary search divides the array into halves to find the target more efficiently.

# def binary_search(arr, low, high, target):
#     if low > high:  
#         return -1
#     mid = (low + high) // 2  

#     if arr[mid] == target:  
#         return mid
#     elif arr[mid] > target: 
#         return binary_search(arr, low, mid - 1, target)
#     else:  
#         return binary_search(arr, mid + 1, high, target)


# arr = [2, 4, 6, 8]
# target = 6
# print(binary_search(arr, 0, len(arr) - 1, target))  


# Write a recursive function to flatten a list containing nested lists.
# For example, the list [1, [2, [3, [4]]], 5] should become [1, 2, 3, 4, 5].

# def flatten_list(lst: list)->list:
#     if len(lst) == 0:  
#         return []
    
#     if isinstance(lst[0], list):  
#         return flatten_list(lst[0]) + flatten_list(lst[1:])
    
#     return [lst[0]] + flatten_list(lst[1:]) 


# print(flatten_list([1, [2, [3, [4]]], 5]))  




# Write a recursive function to find the maximum element in a list.
# For example, in the list [3, 1, 4, 1, 5], the maximum element is 5.

# def find_max(lst):
#     if len(lst) == 1:  
#         return lst[0]
#     return max(lst[0], find_max(lst[1:]))  


# print(find_max([3, 1, 4, 1, 5]))  

