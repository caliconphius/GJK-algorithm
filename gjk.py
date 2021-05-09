
# import libraries
import numpy as np
import matplotlib.pyplot as plt

# point type
class point():
    """ Object representing a point in n-dimensional space:

        Attributes:
        -----------
        dimension : int
            dimension of space point is embedded in
        location : array
            array of values specifying cartesion coordinates of point
        
    """
    def __init__(self, position):
        # dimension of point
        self.dimension = len(position)

        # list of points cartesian coordinates
        self.location = position



class convex_hull():
    """ Object representing the convex hull of a set of points inputted into the    

        Attributes:
        -----------
        dimension : int
            dimension of points are embedded in
        location : array
            array of values specifying cartesion coordinates of point
        
    """    
    def __init__(self,point_list):
        
        # make sure there are at least 3 points
        if len(point_list)<3:
            raise ValueError()

        # dimension of convex hull
        self.dimension = point_list[0].dimension


    

    def add_point(self,p:point):
