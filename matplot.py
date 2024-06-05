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
import matplotlib.pyplot as plt

import numpy as np

a = np.array([5,8,2,9,6])

plt.plot(a,marker='*')

plt.show()

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