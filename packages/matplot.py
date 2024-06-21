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
'''
Matplotlib Scatter
Creating Scatter Plots
With Pyplot, you can use the scatter() function to draw a scatter plot.

The scatter() function plots one dot for each observation. It needs two arrays of the same length, 
one for the values of the x-axis, and one for values on the y-axis:

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

'''
The observation in the example above is the result of 13 cars passing by.

The X-axis shows how old the car is.

The Y-axis shows the speed of the car when it passes.

Are there any relationships between the observations?

It seems that the newer the car, the faster it drives, 
but that could be a coincidence, after all we only registered 13 cars.
'''
'''
Compare Plots
In the example above, there seems to be a relationship between speed and age, 
but what if we plot the observations from another day as well? 
Will the scatter plot tell us something else?
'''

# Example
# Draw two plots on the same figure:

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

'''
Colors
You can set your own color for each scatter plot with the color or the c argument:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()


'''
Color Each Dot
You can even set a specific color for each dot by using an array of colors as value for the c argument:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()


'''
ColorMap
The Matplotlib module has a number of available colormaps.

A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

Here is an example of a colormap:

This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.

How to Use the ColorMap
You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:


'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()
'''
You can include the colormap in the drawing by including the plt.colorbar() statement:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()


'''
Name		 	Reverse	
Accent		 	Accent_r	
Blues		 	Blues_r	
BrBG		 	BrBG_r	
BuGn		 	BuGn_r	
BuPu		 	BuPu_r	
CMRmap		 	CMRmap_r	
Dark2		 	Dark2_r	
GnBu		 	GnBu_r	
Greens		 	Greens_r	
Greys		 	Greys_r	
OrRd		 	OrRd_r	
Oranges		 	Oranges_r	
PRGn		 	PRGn_r	
Paired		 	Paired_r	
Pastel1		 	Pastel1_r	
Pastel2		 	Pastel2_r	
PiYG		 	PiYG_r	
PuBu		 	PuBu_r	
PuBuGn		 	PuBuGn_r	
PuOr		 	PuOr_r	
PuRd		 	PuRd_r	
Purples		 	Purples_r	
RdBu		 	RdBu_r	
RdGy		 	RdGy_r	
RdPu		 	RdPu_r	
RdYlBu		 	RdYlBu_r	
RdYlGn		 	RdYlGn_r	
Reds		 	Reds_r	
Set1		 	Set1_r	
Set2		 	Set2_r	
Set3		 	Set3_r	
Spectral		 	Spectral_r	
Wistia		 	Wistia_r	
YlGn		 	YlGn_r	
YlGnBu		 	YlGnBu_r	
YlOrBr		 	YlOrBr_r	
YlOrRd		 	YlOrRd_r	
afmhot		 	afmhot_r	
autumn		 	autumn_r	
binary		 	binary_r	
bone		 	bone_r	
brg		 	brg_r	
bwr		 	bwr_r	
cividis		 	cividis_r	
cool		 	cool_r	
coolwarm		 	coolwarm_r	
copper		 	copper_r	
cubehelix		 	cubehelix_r	
flag		 	flag_r	
gist_earth		 	gist_earth_r	
gist_gray		 	gist_gray_r	
gist_heat		 	gist_heat_r	
gist_ncar		 	gist_ncar_r	
gist_rainbow		 	gist_rainbow_r	
gist_stern		 	gist_stern_r	
gist_yarg		 	gist_yarg_r	
gnuplot		 	gnuplot_r	
gnuplot2		 	gnuplot2_r	
gray		 	gray_r	
hot		 	hot_r	
hsv		 	hsv_r	
inferno		 	inferno_r	
jet		 	jet_r	
magma		 	magma_r	
nipy_spectral		 	nipy_spectral_r	
ocean		 	ocean_r	
pink		 	pink_r	
plasma		 	plasma_r	
prism		 	prism_r	
rainbow		 	rainbow_r	
seismic		 	seismic_r	
spring		 	spring_r	
summer		 	summer_r	
tab10		 	tab10_r	
tab20		 	tab20_r	
tab20b		 	tab20b_r	
tab20c		 	tab20c_r	
terrain		 	terrain_r	
twilight		 	twilight_r	
twilight_shifted		 	twilight_shifted_r	
viridis		 	viridis_r	
winter		 	winter_r
'''
'''
Size
You can change the size of the dots with the s argument.

Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

Example
Set your own size for the markers:
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()

'''
Alpha
You can adjust the transparency of the dots with the alpha argument.

Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:

Example
Set your own size for the markers:

'''


import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

'''
Combine Color Size and Alpha
You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent:

Example
Create random arrays with 100 values for x-points, y-points, colors and sizes:


'''


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()


'''
Matplotlib Bars
Creating Bars
With Pyplot, you can use the bar() function to draw bar graphs:

ExampleGet your own Python Server
Draw 4 bars:



'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

'''
Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

'''
Bar Color
The bar() and barh() take the keyword argument color to set the color of the bars:

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

'''
Color Names
You can use any of the color names.

Example
Draw 4 "hot pink" bars:


'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

'''
Color Hex
Or you can use Hexadecimal color values:

Example
Draw 4 bars with a beautiful green color:

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()

'''
Bar Width
The bar() takes the keyword argument width to set the width of the bars:

Example
Draw 4 very thin bars:


'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

'''
Bar Height
The barh() takes the keyword argument height to set the height of the bars:

Example
Draw 4 very thin bars:


'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()


'''
Matplotlib Histograms
Histogram
A histogram is a graph showing frequency distributions.

It is a graph showing the number of observations within each given interval.

Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
'''

'''
Create Histogram
In Matplotlib, we use the hist() function to create histograms.

The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.

For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10.
'''

import numpy as np

x = np.random.normal(170, 10, 250)

print(x)

'''
The hist() function will read the array and produce a histogram:

Example
A simple histogram:


'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

'''
Matplotlib Pie Charts
Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:
'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

'''
Labels
Add labels to the pie chart with the labels parameter.

The labels parameter must be an array with one label for each wedge:

Example
A simple pie chart:


'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 


'''
Example
Start the first wedge at 90 degrees:


'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

'''
Explode
Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.

The explode parameter, if specified, and not None, must be an array with one value for each wedge.

Each value represents how far from the center each wedge is displayed:

Example
Pull the "Apples" wedge 0.2 from the center of the pie:


'''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 


'''
Shadow
Add a shadow to the pie chart by setting the shadows parameter to True:

Example
Add a shadow:


'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 


'''
Colors
You can set the color of each wedge with the colors parameter.

The colors parameter, if specified, must be an array with one value for each wedge:

Example
Specify a new color for each wedge:

'''


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 
