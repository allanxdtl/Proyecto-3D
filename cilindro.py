from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cilindro:
    def drawCilindro(self, color, base_radius, height, slices, stacks):
        glColor3f(color[0]/255, color[1]/255, color[2]/255)
        glutSolidCylinder(base_radius, height, slices, stacks)