"""
HW01
@Author: David Tsu
for classifying triangles
"""
import unittest

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three values
    corresponding to the lengths of the three sides of the Triangle. 
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'       
    """
    if not isValidTriangle(a, b, c):
        return 'NotATriangle'
    else:
        if a == b == c:
            return 'Equilateral'
        elif a == b != c or a == c != b or b == c != a:
            return 'Isoceles'
        elif a == 3 and b == 4 and c == 5:
            return 'Right'
        else:
            return 'Scalene'

def isValidTriangle(a, b, c):
    """
    Checks side lengths to determine if triangle is valid or not.
    Invalid if any side <= 0 or if the sum of the two smaller sides < largest side.
    """
    sorted_sides = sorted(a, b, c) # last index is now largest value
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
        return False
    else:
        return True
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testMyTestSet2(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'Scalene','Should be Isoceles')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line