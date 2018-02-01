## IMPORTS GO HERE
from math import pi
## END OF IMPORTS 


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
    area = 2 * pi * radius
    return area
#### End OF MARKER

#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(r):
    circle_parameter = pi * (r**2)
    print "The parameter of the circle with radius",r"is",circle_parameter

    
#### End OF MARKER  




if __name__ == '__main__': 
    print get_area(2) 
    output_parameter(1.0) 

