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
        
        #Brazo derecho
        glPushMatrix()
        glTranslate(2.6, -0.8, -0.050)
        glRotate(90, 0, 1, 0)
        glRotate(1, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1.5, 100, 100)
        glTranslate(0, 0, 1)
        glRotate(-1, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1, 100, 100)
        glTranslate(0, 0, 1)
        glRotate(-4.5, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.6, 1, 100, 100)
        glTranslate(0, 0, 1)
        circulos.drawSphere([255,255,255], 0.6, 100, 100)
        glPopMatrix()
        
        #Pelota
        glPushMatrix()
        glTranslate(-4, -2.4, 1.5)
        circulos.drawSphere([250,80,74], 1.5, 100, 100)
        glPopMatrix()