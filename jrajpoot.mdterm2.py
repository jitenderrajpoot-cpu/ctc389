#Jitender Rajpoot
#Midterm Q2

#Define a function to calculate the area of a rectangle.
def area_rectangle(width, length):
    area = width * length
    return area


#In the main part of your program ask the user to enter the base and height of the rectangle.
base = float(input("Enter the base of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

#Call the function and pass the user variables to it. All function variable names must be different from the main part of the program.
product = area_rectangle(base, height) 

#The function will return the result to the main part of the program where you will display it to the user.
print("The area of the rectangle is ", product)
