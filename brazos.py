from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Brazos:
    def DibujarBrazos(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Brazo izquierdo
        glPushMatrix()
        glTranslate(-4, -1.2, -0.050)
        glRotate(90, 0, 1, 0)
        glRotate(-15, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, -0.2, -1)
        glRotate(-8, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, 0, -0.5)
        cilindritos.drawCilindro([255,255,255], 0.6, 0.5, 100, 100)
        circulos.drawSphere([255,255,255], 0.6, 100, 100)
        glPopMatrix()