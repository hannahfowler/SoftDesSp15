"""Dealing with rectangles"""

## Point and print_point from Think Python
class Point(object):
    """Represents a point in 2-D space"""
    pass

class Rectangle(object):
	"""Represents a rectangle.

	attributes: width, height, center"""
	pass 

def print_point(p):
    """Print a Point object in human-readable format"""
    template = "({x}, {y})"
    # See Python string formatting docs
    # https://docs.python.org/2/library/string.html#format-examples
    print template.format(x=p.x, y=p.y)


## TODO:
# - Implement Rectangle class using two points, instead of point + width/length
# - Implement print_rectangle
# - Implement find_center function

def find_center(my_rect):
    """
    Return the Point at the center of my_rect Rectangle

    Note: Your doctest may be different depending on your 
    implementation of Rectangle
    >>> p1 = Point()
    >>> p1.x = 0
    >>> p1.y = 0
    >>> p2 = Point()
    >>> p2.x = 6
    >>> p2.y = 4
    >>> rect = Rectangle()
    >>> rect.lower_left = p1
    >>> rect.upper_right = p2
    >>> print find_center(rect)
    (3.0, 2.0)
    """
    midpoint = Point()
    midpoint.x = 0.5*(p2.x - p1.x)
    midpoint.y = 0.5*(p2.y - p1.y)
    print_point(midpoint)
p1 = Point()
p1.x = 0
p1.y = 0
p2 = Point()
p2.x = 6
p2.y = 4
rect = Rectangle()
find_center(rect)
## Challenge problem:
def bounding_box(rects):
    """
    Given a list of Rectangles, return a Rectangle
    that contains all of them
    """
    pass