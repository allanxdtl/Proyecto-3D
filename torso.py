from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Torso:
    def DibujarTorso(self):
     cubitos = Cube()
     cilindritos = Cilindro()
     circulos = Sphere()
     
     glPushMatrix()
     glTranslate(0, -4.3, 0)
     glRotate(5, 0, 1, 0)
     cubitos.drawCubo([255,255,255], 5)
     glPopMatrix()