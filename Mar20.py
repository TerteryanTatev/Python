# Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
# Call the function with three numbers.
# Call the function with no arguments and ensure it handles this case gracefully.

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1,2,3)) 
# print(sum_numbers())  

# Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
# Call the function with keyword arguments such as name="Alice", age=20, and major="CS".
# Experiment with passing different sets of keyword arguments.

# def display_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# display_student_info(name="Alice", age=20, major="CS")
# display_student_info(city="Erevan", hobby="Photography", favorite_color="Blue")

# Write a function order_item that accepts:
# A required item argument.
# A quantity argument with a default value of 1.
# Arbitrary positional arguments (*args) to specify additional options.
# Arbitrary keyword arguments (**kwargs) for customization details.


# def order_item(item, quantity=1, *args, **kwargs):
#     print(f"Item: {item}")
#     print(f"Quantity: {quantity}")

#     if args:
#         print("Options:", ", ".join(args))

#     if kwargs:
#         print("Customizations:")
#         for key, value in kwargs.items():
#             print(f"{key}: {value}")

# order_item("Burger", 2, "Extra Cheese", "No Pickles", size="Large")
# order_item("Coffee", sugar="Less")


# Write a function register_user that accepts:
# A required positional argument: username.
# A required keyword-only argument: email.
# Hint: Use * to enforce keyword-only arguments.


# def register_user(username, *, email):
#     print(f"Username: {username}")
#     print(f"Email: {email}")

# register_user("john_doe", email="john@example.com")


# Analyze the following code, explain why it raises an error, and fix the function call: 
# def book_ticket(destination, price, discount=0, *extras, **details):
#     print(extras)
#     print(f"Booking to {destination} for ${price - discount}")
#     if extras:
#         print(f"Extras: {', '.join(extras)}")
#     if details:
#         print(f"Details: {details}")

# book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)
# Այս օրինակում positional argumentները պետք է լինել keyword argumentներից առաջ։  պետք է պահել ֆունկցիայի արգումենտների հերթականությունը և չկրկնել արգումենտների անունները։
# Այստեղ մենք փորձում ենք  տալ price=100, սակայն սա շփոթմունք է առաջացնում։
# Նույնն էլ վերաբերվում է extras=["window seat", "meal"]։ positional argumentները պետք է արժեքավորել առանց keywordի
# ճիշտ տարբերակը պետք է լինի այսպես

# book_ticket("Paris", 100, 10, "window seat", "meal", seat_type="business class")

# այստեղ destinationին տալիս է "Paris" արժեքը, priceին՝ 100, discountին՝ 10, extrasին՝  "window seat", "meal"(որպես tuple), իսկ detailsին՝ seat_type="business class"(որպես dictionary)



# Implement a function process_data that accepts a mix of positional arguments, default arguments, arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
# Require the first two arguments to be data (a list) and operation (a string that specifies the operation to perform: 'sum', 'multiply', 'filter').
# Optionally accept a threshold parameter with a default value of None. This will only be used for the 'filter' operation.
# Accept additional numbers via *args to be appended to the data list before processing.
# Accept additional processing options through **kwargs, such as:
# reverse (boolean): Whether to reverse the result.
# unique (boolean): Whether to ensure the data list contains unique values before processing.


# ????????????????
# def process_data(data, operation, threshold=None, *args, **kwargs):  
#     data = list(data) + list(args)  

#     if kwargs.get("unique"):  
#         data = list(set(data))  

#     if operation == "sum":  
#         result = sum(data)  
#     elif operation == "multiply":  
#         result = 1  
#         for num in data:  
#             result *= num  
#     elif operation == "filter":  
#         result = [x for x in data if threshold is not None and x > threshold]  
#     else:  
#         result = False 

#     return result[::-1] if kwargs.get("reverse") else result  

# print(process_data([1, 2, 3], "sum", 5, 6, unique=True, reverse=True))  
# print(process_data([1, 2, 3], "multiply", 5, 6, unique=True)) 
# print(process_data([1, 2, 3], "filter", 2, 5, 1, unique=True))  


# Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.

# def counter():  
#     count = 0  

#     def increment():  
#         nonlocal count  
#         count += 1  
#         return count  

#     return increment  

# c = counter()  
# print(c())  
# print(c())  
# print(c())  


# Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.

# def multiplier_function(multiplier):  
    
#     def multiply(number):  
#         return number * multiplier  
    
#     return multiply  

 
# double = multiplier_function(2)  
# triple = multiplier_function(3)  

# print(double(5))  
# print(triple(5))  


 # Write a closure that tracks the number of times a specific function is called.

# def function_tracker():  
#     count = 0  

#     def wrapper():  
#         nonlocal count  
#         count += 1  
#         print(f"Called {count} times")

#     return wrapper  

# def greet(name):  
#     a = function_tracker()
    
#     def result(): 
#         a()
#         return f"Hello, {name}!"  

#     return result


# b = greet('Alice')
# b()
# b()

# c = greet('Bob')
# c()

# Create a closure to calculate running totals. Each call to the inner function should add a number to the total and return the updated total.


# def running_total():  
#     total = 0  

#     def add(number):  
#         nonlocal total  
#         total += number  
#         return total  

#     return add  
 
# counter = running_total()  
# print(counter(5))  
# print(counter(3)) 
# print(counter(10))


# Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.

# def string_editor(initial=""):  
#     text = initial  

#     def edit(action, new_text=""):  
#         nonlocal text  
#         if action == "append":  
#             text += new_text  
#         elif action == "reset":  
#             text = ""  
#         return text  

#     return edit  


# editor = string_editor("Hello")  
# print(editor("append", " World")) 
# print(editor("append", "!"))     

