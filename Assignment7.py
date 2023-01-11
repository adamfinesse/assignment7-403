from rectpack import *
from tkinter import *
import sys

# CustomCanvas will have a constructor which takes two explicit arguments, height and 
# width, which are expected to be of type int. The constructor will create and display a new Canvas 
# object with the height and width provided. To do this, you will use Canvas, a built-in object 
# defined in the python package tkinter. Documentation for the Canvas class can be found here:
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
class CustomCanvas:
    def __init__(self,heightP,widthP):
        #make the canvas from tk and have it as attributes
        top = Tk()
        self.topObject= top
        self.canvasObject = Canvas(top,bg = "pink",height = heightP,width = widthP)

# Rectangle will have a constructor which takes four explicit parameters, height, width, x, 
# and y. All four arguments are expected to be of type int. x and y represent the origin point of the 
# given rectangle. The origin point will be the upper left corner. Parameters x and y should have 
# default values of zero. The values received as parameters should be stored in instance variables 
# of the same name.  
class Rectangle:
    def __init__(self,heightP,widthP,xP = 0 ,yP = 0):
        self.height = heightP
        self.width = widthP
        self.x = xP
        self.y = yP

# The pack function will have two parameters, allRect and canvasSize. allRect will be a list 
# of Rectangle objects and canvasSize a tuple containing a canvas’ height and width (in that order). 
# pack will take the given list of rectangles and determine a location for each rectangle so that each 
# rectangle does not overlap another and each rectangle exists within the given canvas size. pack 
# will then return a list of placed Rectangle objects. Each given rectangle must be included in the 
# returned list. (Note: Each given rectangle is referring to the logical concept of the rectangle shape 
# not the specific Rectangle object. Two Rectangle objects are logically equivalent if they have the 
# same height and width. When generating the list of Rectangles to return, you can modify the 
# given Rectangle objects or create new, but logically equivalent, Rectangle objects)  

def pack(allRect, canvasSize):
    #create the packer to help store all rects in our bin.
    packer = newPacker()
    for r in allRect:
        packer.add_rect(height= r.height,width=r.width)

    #add our bin (canvas dimensions) to the packer
    packer.add_bin(height= canvasSize[0], width=canvasSize[1])

    #start packing
    packer.pack()

    #after packing create the new list of rectangle objects and return them.
    newRectArr = []
    for rect in packer[0]:
        newRectArr.append(Rectangle(rect.height,rect.width,rect.x,rect.y))

    #after creating all new rects return the new rect array
    return newRectArr

# The main function will read in a filepath as a command line argument. You may assume 
# the filepath is always the second command line argument given (the first being the name of the 
# class being executed) The given filepath will point to a txt file containing a canvas size and 
# rectangles. The first line of the given text file will contain two int’s separated by a comma. 
# These int’s represent a canvas’ height and width (in that order) All following lines represent the 
# height and width of an individual rectangle. main should parse the data in the file and use the 
# information to create a new CustomCanvas object and a new list of Rectangles. Once generated, 
# the list of Rectangles and the size of the canvas should be passed to the pack function. Main 
# should then print each Rectangle contained in the retuned list to the instantiated CustomCanvas 
# object. Each printed Rectangle should have a black border and a colored (not black or white) 
# fill. Main should be called whenever Assignment7.py is run as a stand-alone file but not when 
# Assignment7.py is loaded as a library.

def main(filepath):
    print(filepath)
    #inital rect arr
    rectArr = []

    #open filepath from args and get all the lines in an array
    file = open(filepath,'r')
    lines = file.readlines()

    #make the canvas object and size tuple as its the first line and remove it from lines arr
    canvasDimensions = lines[0].strip().split(',')
    canvasDimensionsTuple = (int(canvasDimensions[0]),int(canvasDimensions[1]))
    canvas = CustomCanvas(canvasDimensions[0],canvasDimensions[1])
    lines.pop(0)

    #for each line after make a rectangle object with the given params
    for index, line in enumerate(lines):
        rectDimensions = line.strip().split(",")
        rectArr.append(Rectangle(int(rectDimensions[0]),int(rectDimensions[1])))

    #now call pack with the constructed rects and canvas and set the result to rectArr
    rectArr = pack(rectArr,canvasDimensionsTuple)

    #add each rect to the canvas. Stack overflow for the win: https://stackoverflow.com/questions/42039564/tkinter-canvas-creating-rectangle
    for rect in rectArr:
        canvas.canvasObject.create_rectangle(rect.x, rect.y ,rect.x + rect.width, rect.y + rect.height, fill="red")

    #now show the canvas with all the rects added
    canvas.canvasObject.pack()
    canvas.topObject.mainloop()
    
if __name__ == "__main__":
    main(sys.argv[1])