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
        glTranslate(0, 2, 0)
        
        glPushMatrix()
        glTranslate(-1, -4.3, 0)
        glRotate(90, 1, 0, 0)
        glRotate(-10, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 1.4, 1.6, 100, 100)
        glPopMatrix()
        
        glPushMatrix()
        glTranslate(1, -4.3, 0)
        glRotate(90, 1, 0, 0)
        glRotate(10, 0, 1, 0)
        cilindritos.drawCilindro([111,84,187], 1.4, 1.6, 100, 100)
        glPopMatrix()
        
        glPopMatrix()
        
        #Pierna izquierda
        glPushMatrix()
        glTranslate(-1.3, -3.9, 0)
        glRotate(90, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.8, 1.4, 100, 100)
        glTranslate(0,0.5,1.2)
        glScale(1,1,0.4)
        circulos.drawSphere([255,255,255], 0.8, 100, 100)
        glPopMatrix()
        
        #Pierna derecha
        glPushMatrix() #Matrix para rotar la pierna
        glRotate(10, 0, 0, 1)
        glTranslate(-0.8, 0, 0)
        
        glPushMatrix()
        glTranslate(1.3, -3.9, 0)
        glRotate(90, 1, 0, 0)
        cilindritos.drawCilindro([255,255,255], 0.8, 1.4, 100, 100)
        glTranslate(0,0.5,1.2)
        glScale(1,1,0.4)
        circulos.drawSphere([255,255,255], 0.8, 100, 100)
        glPopMatrix()
        
        glPopMatrix() #Fin de matrix para rotar pierna
        
        #Base figura
        glPushMatrix()
        glTranslate(0, -5.5, 0)
        glRotate(90, 1, 0, 0)
        cilindritos.drawCilindro([253, 194, 104], 4, 1, 100, 100)
        glPopMatrix()
        