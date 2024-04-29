from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Sphere:
    def drawSphere(self, color, radio, slices, stacks):
        glColor3f(color[0]/255, color[1]/255, color[2]/255)
        glutSolidSphere(radio, slices, stacks)