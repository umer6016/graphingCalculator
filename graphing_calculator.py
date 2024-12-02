import numpy as np
import matplotlib.pyplot as plt

#had to add the dictionary for UX and security purposes
math_funcs = {
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "log": np.log,
    "log10": np.log10,
    "sqrt": np.sqrt,
    "sinh": np.sinh,
    "cosh": np.cosh,
    "tanh": np.tanh,
    "arcsin": np.arcsin,
    "arccos": np.arccos,
    "arctan": np.arctan,
    "arcsinh": np.arcsinh,
    "arccosh": np.arccosh,
    "arctanh": np.arctanh,
    "pi": np.pi,
    "e": np.e
}

print("-----Graphing Calculator-----")
print("The functions supported for this versiona are:")
#Printing the supported functions
for key in math_funcs:
    print(f"To use use {key} write {key}(x)")
print("To raise x to a power write it as x**exponent i.e x**4")
print("-----------------------------------------------------------------------------------")
funcInp = input("Enter a mathematical function in terms of x: ")

#Taking the range from the user
x_min = float(input("Enter the min value: "))
x_max = float(input("Enter the max value: "))
points= int(input("Enter the number of points to plot: "))

#Generating the range based on user input
x = np.linspace(x_min,x_max,points)
try:
    #"{__builtins__":None} is for security reasons to prevent malicious input
    #dictionary unpacking makes all the functions available in this scope
    y = eval(funcInp, {"__builtins__": None}, {"x": x, **math_funcs})
    #Hide invalid values
    y = np.ma.masked_invalid(y)  
except Exception as e:
    print(f"Error evaluating the function '{funcInp}': {e}")
    exit()

#Graphing stuff using matplotlib
plt.plot(x,y)
plt.title(f"Graph of {funcInp}")
plt.xlabel('x')
plt.ylabel(f"y = f(x) = {funcInp}")
plt.grid(True)
plt.show()