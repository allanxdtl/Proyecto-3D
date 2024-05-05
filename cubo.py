from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cube:
    
    def drawCubo(self, color, size):
        glColor3f(color[0]/255, color[1]/255, color[2]/255)
        glutSolidCube(size)