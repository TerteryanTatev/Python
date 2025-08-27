# Implement a function make_greeting(greeting) that takes a greeting string and returns a function
# that takes a name and prints the greeting followed by the name.

def make_greeting(greeting):
    
    
    def username(name):
        print(greeting, name)
     
    return username    


a = make_greeting('hi')
a('Bob')
a('Alice')

# Write a function make_accumulator(start=0) that returns a function which adds its argument to
# start and returns the new total each time it is called.

def  make_accumulator(start=0):
    total_number = start
    def total(num):
       nonlocal  total_number 
       total_number += num
       print(total_number)
    
    return total    


a = make_accumulator()
a(6)
a(8)

# Implement a function make_config(key, value) that returns a function which, when called, 
# returns a dictionary with the given key-value pair.


def make_config(key, value):
    
    def print_result():
    
        print(f"{key} - {value}")
        
    return print_result    
    
    
a = make_config('name', 'Alice')
a()
 