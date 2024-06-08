'''
Matplotlib is a low level graph plotting library in python that serves as a 
visualization utility.

Installation of Matplotlib

------> pip install matplotlib


import matplotlib

Once Matplotlib is installed, 
import it in your applications by adding the import module statement:


'''

# import matplotlib

# print(matplotlib.__version__)

#to verify the matplotlib version


'''
pyplot

Most of the Matplotlib utilities lies under the pyplot submodule, 
and are usually imported under the plt alias:
'''
# import matplotlib.pyplot as plt

# import numpy as np
# x = np.array([0,6])
# y = np.array([0,250])

# plt.plot(x,y)
# plt.show()


'''
Plotting x and y points
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), 
we have to pass two arrays [1, 8] and [3, 10] to the plot function.

'''

# import matplotlib.pyplot as plt
# import numpy as np

# a = np.array([1,8])
# b = np.array([3,10])

# plt.plot(a,b)
# plt.show()


'''
Markers

you can use the key word argument marker to emphasize each point with specified marker.

'''
# import matplotlib.pyplot as plt

# import numpy as np

# a = np.array([5,8,2,9,6])

# plt.plot(a)

# plt.show()

'''
now you will get the output but not as markers , so we have to mark it
----> plt.plot(a,marker ='o')
'''

# import matplotlib.pyplot as plt

# import numpy as np

# a = np.array([5,8,2,9,6])

# plt.plot(a,marker='o')

# plt.show()

'''
--->marker = '*'

'''
# import matplotlib.pyplot as plt

# import numpy as np

# a = np.array([5,8,2,9,6])

# plt.plot(a,marker='*')

# plt.show()

'''
Marker Reference
You can choose any of these markers:

Marker	Description
'o'	--> Circle	
'*'	--> Star	
'.'	--> Point	
','	--> Pixel	
'x'	--> X	
'X'	--> X (filled)	
'+'	--> Plus	
'P'	--> Plus (filled)	
's'	--> Square	
'D'	--> Diamond	
'd'	--> Diamond (thin)	
'p'	--> Pentagon	
'H'	--> Hexagon	
'h'	--> Hexagon	
'v'	--> Triangle Down	
'^'	--> Triangle Up	
'<'	--> Triangle Left	
'>'	--> Triangle Right	
'1'	--> Tri Down	
'2'	--> Tri Up	
'3'	--> Tri Left	
'4'	--> Tri Right	
'|'	--> Vline	
'_'	--> Hline

'''


'''
Line plot
'''
################################################08/06/24
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# # plt.plot(ypoints, linestyle = 'dotted') # it is for dotted
# # plt.show()

# plt.plot(ypoints, linestyle = 'dashed') # it is for dashed
# plt.show()

'''
Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.
'''

'''
Line Styles
You can choose any of these styles:

Style	Or
'solid' (default) --->	'-'	
'dotted'	      ===>  ':'	
'dashed'	      --->  '--'	
'dashdot'	      --->  '-.'	
'None'	          ===>  '' or ' '	
'''
'''
Line Color

You can use the keyword argument color or the shorter c to set the color of the line:
'''
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r')
# plt.show()

'''
You can also use Hexadecimal color values:
'''
# plt.plot(ypoints, c = '#4CAF50')
# plt.show()


'''
Plot with the color named "hotpink":
'''

# plt.plot(ypoints, c = 'hotpink')
# plt.show()

'''
Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:
'''

# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

'''
Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:

'''

# import matplotlib.pyplot as plt
# import numpy as np

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

'''
You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)

The x- and y- values come in pairs:
'''
# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()


'''
Matplotlib label and title
'''

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()


'''
Create a Title for a Plot
With Pyplot, you can use the title() function to set a title for the plot.
'''
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()


'''
Set Font Properties for Title and Labels
You can use the fontdict parameter in xlabel(), ylabel(), and title() 
to set font properties for the title and labels.
'''

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.show()


'''
Position the Title
You can use the loc parameter in title() to position the title.

Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()


'''
Matplotlib Adding Grid Lines

'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()



'''
Specify Which Grid Lines to Display
You can use the axis parameter in the grid() function to specify which grid lines to display.

Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()



'''
Display only grid lines for the x-axis:
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()

'''
Display only grid lines for the y-axis:
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()

'''
Matplotlib Subplot
Display Multiple Plots
With the subplot() function you can draw multiple plots in one figure:

ExampleGet your own Python Server
Draw 2 plots:
'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()


'''
The subplot() Function
The subplot() function takes three arguments that describes the layout of the figure.

The layout is organized in rows and columns, which are represented by the first and second argument.

The third argument represents the index of the current plot.
'''
plt.subplot(1, 2, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.

plt.subplot(1, 2, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
#So, if we want a figure with 2 rows an 1 column (meaning that the two plots will be displayed on top of each other instead of side-by-side), we can write the syntax like this:
'''
Example
Draw 2 plots on top of each other:
'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()
'''


You can draw as many plots you like on one figure, just descibe the number of rows, columns, and the index of the plot.

Example
Draw 6 plots:
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()
'''


Title
You can add a title to each plot with the title() function:

Example
2 plots, with titles:
'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()


'''
Super Title
You can add a title to the entire figure with the suptitle() function:

Example
Add a title for the entire figure:
'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
