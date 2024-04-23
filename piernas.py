from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Piernas:
    def DibujarPiernas(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Pantalones
        glPushMatrix()
        glTranslate(-1, -4.3, 0)
        glRotate(90, 1, 0, 0)
        glRotate(-10, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 1.8, 1.6, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(1, -4.3, 0)
        glRotate(90, 1, 0, 0)
        glRotate(10, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 1.8, 1.6, 100, 100)
        glPopMatrix()
        
        #Pierna izquierda
        glPushMatrix()
        glTranslate(-1.3, -4.2, 0)
        glRotate(90, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1, 100, 100)
        glPopMatrix()