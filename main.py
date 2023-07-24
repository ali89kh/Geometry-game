from random import randint
import turtle


# Class representing a Point with x and y coordinates
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Check if the Point falls inside a given Rectangle
    def point_fall(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and \
           rectangle.point1.y < self.y < rectangle.point2.y:
            return "It is inside the rectangle."
        else:
            return "It is outside the rectangle."


# Class representing a Rectangle with two Points defining opposite corners
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


# Class representing a GUI Rectangle, inheriting from Rectangle
class GuiRectangle(Rectangle):
    # Draw the GUI Rectangle on the canvas
    def draw(self, canvas):
        canvas.penup()
        # Go to a certain coordinate
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


# Class representing a GUI Point, inheriting from Point
class GuiPoint(Point):
    # Draw the GUI Point on the canvas
    def draw(self, canvas, size=5, color="red"):
        canvas.penup()
        # Go to a certain coordinate
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


# Generate a random Rectangle and a random Point
rectangle = Rectangle(Point(randint(0, 300), randint(0, 300)), Point(randint(300, 400), randint(300, 400)))
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))

# Print the coordinates of the Rectangle
print(rectangle.point1.x, rectangle.point1.y, rectangle.point2.x, end=" ")
print(rectangle.point2.y)
# Check if the user's Point is inside the Rectangle and print the result
print(user_point.point_fall(rectangle))

# Initialize the turtle graphics
my_turtle = turtle.Turtle()

# Create a GUI Rectangle instance and draw it
rectangle_gui = GuiRectangle(rectangle.point1, rectangle.point2)
rectangle_gui.draw(canvas=my_turtle)

# Draw the user's GUI Point on the canvas
user_point.draw(canvas=my_turtle)

# Finish drawing and display the GUI
turtle.done()
