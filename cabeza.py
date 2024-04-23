from cubo import Cube
from circulos import Sphere
from cilindro import Cilindro
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cabeza:
    def DibujarCabeza(self):
        cubitos = Cube()
        cilindritos = Cilindro()
        circulos = Sphere()
        
        #Cabeza
        circulos.drawSphere([239,238,244], 5, 100, 100)
        glPushMatrix()
        glTranslate(3, 0.3, -0.45)
        
        #Ojo derecho y pupila
        cilindritos.drawCilindro([111,84,187], 1, 5, 100, 100)
        glTranslate(0,0, 0.01)
        cilindritos.drawCilindro([255,255,255], 0.40, 5, 100, 100)
        
        #Ceja derecha
        glTranslate(-1, 0.9, 5)
        glRotate(90, 0, 1, 0)
        glRotate(-30, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.80, 100, 100)
        
        glTranslate(0,0,0.78)
        glRotate(14, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.5, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(30, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(30, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        glPopMatrix()
        
        #Ojo izquierdo
        glPushMatrix()
        
        glPushMatrix()
        glTranslate(-2.5, 0, 5)
        glRotate(90, 0, 1, 0)
        glRotate(-20, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        
        glTranslate(0,0, 0.50)
        glRotate(18, 1, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        
        glTranslate(0,0,0.50)
        glRotate(20, 0.50, 0, 0)
        cilindritos.drawCilindro([111,84,187], 0.20, 0.7, 100, 100)
        glPopMatrix()
        glPopMatrix()
        
        #Ceja izquierda
        glPushMatrix()
        glTranslatef(0, 0,5.012)
        glTranslatef(-2.1, 1.9, -0.1)
        glRotatef(90, 0, 1, 0)
        glRotatef(30, 1,0,0)
        cilindritos.drawCilindro([111,84,187], 0.2, 1.9, 100, 100)
        glPopMatrix()
        
        """Torso temporal
        mover esto a su respectiva clase cuando se pueda"""
        glTranslate(0, -4.3, 0)
        glRotate(5, 0, 1, 0)
        cubitos.drawCubo([255,255,255])
       