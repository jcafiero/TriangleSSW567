# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(12,12,12),'Equilateral','12,12,12 should be equilateral')
    
    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(4,4,3),'Isosceles','4,4,3 should be isoceles')
        self.assertEqual(classifyTriangle(9,10,10),'Isosceles','9,10,10 should be isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(5,6,8),'Scalene','5,6,8 should be scalene')
        self.assertEqual(classifyTriangle(2,6,7),'Scalene','2,6,7 should be scalene')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle','1,1,2 is not a triangle')
        self.assertEqual(classifyTriangle(4,4,20),'NotATriangle','4,4,20 is not a triangle')

    def testValidInput(self):
        self.assertEqual(classifyTriangle(500,500,500),'InvalidInput','500,500,500 is invalid input')
        self.assertEqual(classifyTriangle('250',25,25),'InvalidInput',"'250',250,250 is invalid input")
        self.assertEqual(classifyTriangle(-5,3,4),'InvalidInput','-5,3,4 is invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

