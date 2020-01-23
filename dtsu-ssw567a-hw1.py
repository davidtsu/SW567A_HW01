"""
HW01
@Author: David Tsu
using template provided by jrr
for classifying triangles
"""
import unittest

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three values
    corresponding to the lengths of the three sides of the Triangle. 
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'       
    """
    if not isValidTriangle(a, b, c):
        return 'NotATriangle'
    else:
        sorted_sides = sorted([a, b, c]) # largest side is now last index
        if a == b == c:
            return 'Equilateral'
        elif a == b != c or a == c != b or b == c != a:
            return 'Isosceles'
        elif sorted_sides[0]**2 + sorted_sides[1]**2 == sorted_sides[2]**2: # a^2 + b^2 = c^2
            return 'Right'
        else:
            return 'Scalene'

def isValidTriangle(a, b, c):
    """
    Checks sides to determine if triangle is valid or not.
    Invalid if non-numerical value, if any side <= 0, or if the sum of the two smaller sides < largest side.
    """
    try:
        sorted_sides = sorted([float(a), float(b), float(c)]) # last index is now largest value
    except ValueError:
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif sorted_sides[0] + sorted_sides[1] <= sorted_sides[2]:
        return False
    else:
        return True
            
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testEquilateral(self): # test equilateral triangle
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        self.assertEqual(classifyTriangle(2.5,2.5,2.5),'Equilateral','2.5,2.5,2.5 is an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(2,2,3),'Equilateral','2,2,3 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(-1,-1,-1),'Equilateral','-1,-1,-1 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle(0,0,0),'Equilateral','0,0,0 is not an Equilateral triangle')
        self.assertNotEqual(classifyTriangle('a','a','a'),'Equilateral','a,a,a is not an Equilateral triangle')

    def testisosceles(self): # test Isosceles triangle
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(6,7,6),'Isosceles','6,7,6 is an Isosceles triangle')
        self.assertEqual(classifyTriangle(4,3,3),'Isosceles','4,3,3 is an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(2,2,-3),'Isosceles','2,2,-3 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(-2,-2,-3),'Isosceles','-2,-2,-3 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle(0,0,1),'Isosceles','0,0,1 is not an Isosceles triangle')
        self.assertNotEqual(classifyTriangle('a','a','b'),'Isosceles','a,a,b is not an Isosceles triangle')

    def testRight(self): # test right triangle
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(6,8,10),'Right','6,8,10 is a Right triangle')
        self.assertNotEqual(classifyTriangle(3,4,-5),'Right','3,4,-5 is not a Right triangle')
        self.assertNotEqual(classifyTriangle(-6,-8,-10),'Right','-6,-8,-10 is not a Right triangle')
        self.assertNotEqual(classifyTriangle(0,1,1),'Right','0,1,1 is not a Right triangle')

    def testScalene(self): # test scalene triangle
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')
        self.assertEqual(classifyTriangle(7,6,5),'Scalene','7,6,5 is a Scalene triangle')
        self.assertEqual(classifyTriangle(8,9,10),'Scalene','8,9,10 is a Scalene triangle')
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a Scalene triangle')
        self.assertNotEqual(classifyTriangle(6,7,-8),'Scalene','6,7,-8 is not a Scalene triangle')
        self.assertNotEqual(classifyTriangle(-9,-10,-11),'Scalene','-9,-10,-11 is not a Scalene triangle')

    def testNotATriangle(self): # test invalid triangle and bad input
        self.assertEqual(classifyTriangle(1,3,0),'NotATriangle','1,3,0 is NotATriangle')
        self.assertEqual(classifyTriangle(0,0,0),'NotATriangle','0,0,0 is NotATriangle')
        self.assertEqual(classifyTriangle(1,1,10),'NotATriangle','1,1,10 is NotATriangle')        
        self.assertEqual(classifyTriangle(1,3,5),'NotATriangle','1,3,5 is NotATriangle')
        self.assertEqual(classifyTriangle(-2,3,-4),'NotATriangle','-2,3,-4 is NotATriangle')        
        self.assertEqual(classifyTriangle(-1,3,5),'NotATriangle','-1,3,5 is NotATriangle')
        self.assertEqual(classifyTriangle('a','b','c'),'NotATriangle','a,b,c is NotATriangle')

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(2,2,3)
    runClassifyTriangle(2,2,4)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from IDE
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line