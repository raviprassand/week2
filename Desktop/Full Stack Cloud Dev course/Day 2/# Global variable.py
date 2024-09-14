# Global variable
x = "global"

def my_function():
    # Local variable
    x = "local"
    print("Inside function:", x)

my_function()
print("Outside function:", x)