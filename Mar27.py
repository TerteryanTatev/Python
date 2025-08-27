#  Write a Python function named custom_filter that replicates the behavior of the built-in filter function.


# def custom_filter(func, iterable):
#     result = []
#     if callable(func):
#       for item in iterable:
#          if func(item):
#              result.append(item)
      
#     else:
#          for item in iterable:
#            if item:
#              result.append(item)
#     return result

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# print(custom_filter(is_even, numbers))

# Write a Python function named custom_map that replicates the behavior of the built-in map function. 

# def custom_map(func, iterable):
#     if func is None:
#        return iterable
    
#     result = []
#     for item in iterable:
#         result.append(func(item))  
#     return result

# def square(x):
#     return x ** 2

# numbers = [1, 2, 3, 4]
# result = custom_map(square, numbers)
# print(result) 

#  Write a Python function named custom_zip that replicates the behavior of the built-in zip function.


# def custom_zip(*iterables):
#     result = []
#     min_length = min(len(i) for i in iterables)

#     for i in range(min_length):
#         result.append(tuple(j[i] for j in iterables))  

#     return result

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# print(custom_zip(list1, list2)) 


# Write a Python function named custom_reduce that replicates the behavior of the functools.reduce function.

# def custom_reduce(func, iterable):
#     iterator = iter(iterable)
#     accumulator = next(iterator)


#     for item in iterator:
#         accumulator = func(accumulator, item)

#     return accumulator

# def add(x, y):
#     return x + y

# numbers = [1, 2, 3, 4]
# print(custom_reduce(add, numbers)) 

# Write a Python function named custom_enumerate that replicates the behavior of the built-in enumerate function


# def custom_enumerate(iterable, start=0):
#     result = []
#     index = start  
#     for item in iterable:
#         result.append((index, item))
#         index += 1  

#     return result


# fruits = ['apple', 'banana', 'cherry']
# result = custom_enumerate(fruits, start=1)
# print(result)  





# ls = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# sum =0
# for i in range(len(ls)):
#     sum += ls[i][i]

# for i in range(len(ls)):
#     sum += ls[i][len(ls)-1-i]

# def foo(newlist, i=0):
#     if not newlist: 
#         return
    
#     print (newlist[0][len(newlist[0])-1-i])
    
#     foo(newlist[1:], i+1)
# foo(ls)

# def fibonacci(num:int):
#     # print(num)
#     if num == 0 or num ==1:
#         return num
    
#     return fibonacci(num-2) + fibonacci(num-1)


# print(fibonacci(5))


# string = input()


# def findupper(st: str) -> str:#+
#     if not st:
#         return 'string does not have uppercase'#+
#     if st[0].isupper():
#         return st[0]

#     return findupper(st[1:])

    
# print(findupper(string))


