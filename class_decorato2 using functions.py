def decorator_function(original_function):  
    def wrapper_function():
        print("Wrapper executed this")
        return original_function()
    return wrapper_function
def display():
    print("The display function ran")

decorated_display=decorator_function(display)
#decorator_function.display()
decorated_display()
