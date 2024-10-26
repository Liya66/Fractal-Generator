# import tkinter
from tkinter import *
from tkinter.ttk import *
# import turtle
import turtlefigures
from turtle import TurtleScreen, RawTurtle
from tkinter.colorchooser import askcolor
import random


# make the window
root = Tk()
root.title("Turtle Generator")
# make the interface

#make the canvas
canvasFrame=LabelFrame(root, text="Canvas")
canvasFrame.grid(row = 1, column = 0, columnspan = 5, rowspan = 5)
canvas = Canvas(canvasFrame, width = 800, height = 500)
canvas.pack()

#link turtlescreen with the canvas
screen = TurtleScreen(canvas)
screen.bgcolor("black")
w, h = screen.screensize()

#setup the turtle
# make a turtle pen and connected it with the screen
pen = RawTurtle(screen)
pen.color("beige")
pen.speed(0)
pen.width(3)

# Create a function to update the values when sliders are moved
def update_values(event):
    # Get the current values from the sliders
    order = int(orderSlider.get())
    length = int(lengthSlider.get())
    
    # Update your application logic with the new values
    # Replace the following lines with your actual logic
    print("Order:", order)
    print("Length:", length)
    
    # Update the value labels
    order_value_label.config(text=f"Order: {order}")
    length_value_label.config(text=f"Length: {length}")


# Make a control panel
controlFrame = LabelFrame(root, text="Control Panel")
controlFrame.grid(row=0, column=5, columnspan=4, rowspan=4, pady=10, sticky="n")

# Order Slider (0 to 5)

orderSlider = Scale(controlFrame, from_=0, to=5, length=130, orient="horizontal",command=update_values)
orderSlider.grid(row=1, column=0, columnspan=2,sticky="w")

# Length Slider (0 to 800)


lengthSlider = Scale(controlFrame, from_=0, to=800, length=130, orient="horizontal",command=update_values)
lengthSlider.grid(row=2, column=0, columnspan=2,sticky="w")

# Value labels
order_value_label = Label(controlFrame, text=f"Order={int(orderSlider.get())}")
order_value_label.grid(row=1, column=3)

length_value_label = Label(controlFrame, text=f"Length={int(lengthSlider.get())}")
length_value_label.grid(row=2, column=3)

#option menu 

figureNames = ["Binary Tree", "Dandelion", "Fern", "Snowflake","Antiflake", "Gasket3","Gasket4","Gasket6","Circle","Doily","Circle2","Circle4","Flower","Cross","Pentadoily"]
figureStr = StringVar()
figureList = OptionMenu(controlFrame, figureStr, figureNames[0], *figureNames)
figureList.config(width=11)
figureList.grid(row=3, column=0,sticky="w")


def luckyF():
    order = random.randint(1,4)
    length = random.randint(80,270)
    luckyFigure = str(random.choice(figureNames))
  
    if luckyFigure == "Binary Tree":
        display_message("Wow, it's a binary tree!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.right(90);pen.forward(h/3);pen.left(90);pen.down()
        turtlefigures.tree(order, length, pen);
        
    elif luckyFigure == "Dandelion":
        display_message("Wow, it's a dandelion!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.d(order,length, pen)
       
    elif luckyFigure == "Fern":
        display_message("Wow, it's a fern!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.f(order,length, pen)
        
    elif luckyFigure == "Snowflake":
        display_message("Wow, it's a snowflake!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.flake(order,length, pen)
      
    elif luckyFigure == "Antiflake":
        display_message("Wow, it's a antiflake!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.antiflake(order,length, pen)
        
    elif luckyFigure == "Gasket3":
        display_message("Wow, it's a gasket3!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket3(order,length, pen)
        
    elif luckyFigure == "Gasket4":
        display_message("Wow, it's a gasket4!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket4(order,length, pen)
     
    elif luckyFigure == "Gasket6":
        display_message("Wow, it's a gasket6!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket6(order,length, pen)
       
    elif luckyFigure == "Circle":
        display_message("Wow, it's a Circle!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC(order,length, pen)
    
    elif luckyFigure == "Doily":
        display_message("Wow, it's a Doily!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketc3(order,length, pen)
       
    elif luckyFigure == "Circle2":
        display_message("Wow, it's a Circle!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC2(order,length, pen)
     
    elif luckyFigure == "Circle4":
        display_message("Wow, it's a circle4!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC4(order,length, pen)
        
    elif luckyFigure == "Flower":
        display_message("Wow, it's a flower!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.flower(order,length, pen)
        
    elif luckyFigure == "Cross":
        display_message("Wow, it's a cross!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.cross(order,length, pen)
        display_message("abc")
    elif luckyFigure == "Pentadoily":
        display_message("Wow, it's a pentadoily!Find out more by choosing this shape and drawing it!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket5(order,length, pen)
    
def clearF():
    # Clear the sliders
    orderSlider.set(0)
    lengthSlider.set(0)

    # Clear the canvas
   
    pen.clear()

    # Reset the existing turtle and move it back to the center

    pen.penup()
    pen.setpos(0, 0)
    pen.pendown()
   
    
clearButton = Button(controlFrame, text="Clear", command=clearF,width=12)
clearButton.grid(row=5, column=0, columnspan=2,sticky="w")


luckyButton=Button(controlFrame, text="I'm feeling lucky;)", command=luckyF, width=12)
luckyButton.grid(row=4, column=0, columnspan=5,sticky="w")

# Create a Text widget to display the drawing message
message_box = Text(root, height=6, width=28)
message_box.grid(row=5, column=5, columnspan=4,rowspan=2, sticky="w")

# Function to display a message in the message box
def display_message(message):
    message_box.delete(1.0, END)  # Clear the message box
    message_box.insert(END, message)  # Display the new message


def drawF():
    # get the order and length values
    order  = int(orderSlider.get())
    length = int(lengthSlider.get())
    # get the selection index from the option menu

 # get the selection index from the option menu
    figureName = figureStr.get()
    # use the figure index to call the selected turtle method
    if length == 0 :
        messagebox.showerror('Python Error', 'Error: The length cannot be 0!')
    if figureName == "Binary Tree":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. It is one of the most basic figures.")
        pen.up();pen.backward(w/3);pen.right(90);pen.forward(h/3);pen.left(90);pen.down()
        turtlefigures.tree(order, length, pen)
    elif figureName == "Dandelion":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. It is based on the binary tree.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.d(order,length, pen)
    elif figureName == "Fern":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. It is not symmetrical!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.f(order,length, pen)
    elif figureName == "Snowflake":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. Isn't it beautiful?")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.flake(order,length, pen)
    elif figureName == "Antiflake":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}.It's failed attemp of making snow, but it also looks cool")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.antiflake(order,length, pen)
    elif figureName == "Gasket3":
        pen.up();pen.backward(w/3);pen.down()
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. It is the classic Sierpinski gasket.")
        turtlefigures.gasket3(order,length, pen)
    elif figureName == "Gasket4":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. It is made of squres.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket4(order,length, pen)
    elif figureName == "Gasket6":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}.Having six sides makes it more delicate!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket6(order,length, pen)
    elif figureName == "Circle":
        display_message(f"You're drawing a {figureName} with order {order} and length {length}. This is a basic circle figure.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC(order,length, pen)
    elif figureName == "Doily":
        display_message(f"Drawing {figureName} with order {order} and length {length}. This is a variation of circle fractal.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketc3(order,length, pen)
    elif figureName == "Circle2":
        display_message(f"Drawing {figureName} with order {order} and length {length}. This is another variation of circle fractal.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC2(order,length, pen)
    elif figureName == "Circle4":
        display_message(f"Drawing {figureName} with order {order} and length {length}. This is actually easier to draw!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasketC4(order,length, pen)
    elif figureName == "Flower":
        display_message(f"Drawing {figureName} with order {order} and length {length}. Wonderful octagons!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.flower(order,length, pen)
    elif figureName == "Cross":
        display_message(f"Drawing {figureName} with order {order} and length {length}. This looks like a Swiss flag.")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.cross(order,length, pen)
    elif figureName == "Pentadoily":
        display_message(f"Drawing {figureName} with order {order} and length {length}. Wonderful pentagons!")
        pen.up();pen.backward(w/3);pen.down()
        turtlefigures.gasket5(order,length, pen)
# Display a message in the message box
    

# Update the "Draw" button's command to call display_message
drawButton = Button(controlFrame, text="Draw", command=drawF,width=12)
drawButton.grid(row=6, column=0, columnspan=2,sticky="w")
   

# Create a function to change the canvas background color
def change_bg_color():
    color = askcolor()[1]  # Launch the color dialog and get the selected color
    if color:
        canvas.configure(bg=color)  # Set the canvas background color

# Make second control panel
# Create a frame for background color controls
settingsFrame = LabelFrame(root, text="Settings")
settingsFrame.grid(row=3, column=5, columnspan=4, rowspan=4, sticky="nw")

# Add a button to open the color dialog
colorButton = Button(settingsFrame, text="Select Background Color", command=change_bg_color)
colorButton.grid(row=0, column=0,sticky="n")

# Create a function to change the turtle's color
def change_turtle_color():
    color = askcolor()[1]  # Launch the color dialog and get the selected color
    if color:
        pen.color(color)  # Set the turtle's color

# Add a button to change the turtle's color
turtleColorButton = Button(settingsFrame, text="Select Turtle Color", command=change_turtle_color, width="17")
turtleColorButton.grid(row=1, column=0, sticky="w")

orderLabel = Label(settingsFrame, text="Turtle Shape")
orderLabel.grid(row=2, column=0, sticky="w")

# Available turtle shapes
turtle_shapes = ["classic", "turtle", "triangle", "arrow", "square", "circle"]

# Create a StringVar to store the selected shape
selected_shape = StringVar()
selected_shape.set(turtle_shapes[0])  # Set the initial shape

# Function to change the turtle's shape
def change_turtle_shape(shape):
    pen.shape(shape)

# Create radio buttons for turtle shape selection
for i, shape in enumerate(turtle_shapes):
    radio_button = Radiobutton(settingsFrame, text=shape, variable=selected_shape, value=shape, command=lambda s=shape: change_turtle_shape(s))
    radio_button.grid(row=3 + i, column=0, sticky="w")


# loop it
root.mainloop()
